from django.contrib.auth import get_user_model, authenticate
from django.core.mail import send_mail

from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from course_root.settings import EMAIL_HOST_USER

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    password_confirmation = serializers.CharField(required=True, min_length=6)
    first_name = serializers.CharField(required=True, min_length=1)
    last_name = serializers.CharField(required=True, min_length=1)
    male = serializers.CharField(required=True)
    position = serializers.CharField(required=True)

    def validate_email(self, email):
        if User.objects.filter(email=email, is_active=True).exists():
            raise serializers.ValidationError('Адрес почты уже занят')
        return email

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation')
        male = attrs.get('male')
        position = attrs.get('position')
        if password != password_confirmation:
            raise serializers.ValidationError('Пароли не совподают')
        if male not in ('male', 'female'):
            raise serializers.ValidationError('choose valid male')
        if position not in ('student', 'teacher'):
            raise serializers.ValidationError('choose valid position')
        return attrs


    def create(self):
        attrs = self.validated_data
        user = User.objects.create_user(**attrs)
        code = user.generate_activation_code()
        user.send_activation_email(user.email, code)
        return user



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return email

    def validate(self, attrs):
        request = self.context.get('request')
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(username=email, password=password, request=request)
            if not user:
                raise serializers.ValidationError('Неверный email или пароль')
        else:
            raise serializers.ValidationError('Email и пароль обязательны')
        attrs['user'] = user
        return attrs

class ChangePasswordSerializer(serializers.Serializer):
    old_pass = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    password_confirm = serializers.CharField(required=True, min_length=6)

    def validate_old_pass(self, old_pass):
        user = self.context.get('request').user
        if not user.check_password(old_pass):
            raise serializers.ValidationError('Неверный пароль')
        return old_pass

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.get('password_confirm')
        if pass1 != pass2:
            raise serializers.ValidationError('Пароли не совподают')
        return attrs

    def set_new_pass(self):
        user = self.context.get('request').user
        password = self.validated_data.get('password')
        user.set_password(password)
        user.save()


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return email

    def send_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        code = user.generate_activation_code()
        send_mail(
            'Восстановление пароля',
            f'Ваш код потверждения: {code}',
            EMAIL_HOST_USER,
            [email]
        )

class ForgetPasswordCompleteSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    code = serializers.CharField(min_length=8, max_length=8, required=True)
    password = serializers.CharField(required=True)
    password_confirm = serializers.CharField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return email

    def validate_code(self, code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return code

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.get('password_confirm')
        if pass1 != pass2:
            raise serializers.ValidationError('Пароли не совподают')
        return attrs

    def set_new_pass(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.activation_code = ''
        user.save()


class SearchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


