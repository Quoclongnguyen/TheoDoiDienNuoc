from django import forms
from .models import User,ElectricityBill
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'full_name', 'email', 'phone_number', 'address']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Tên đăng nhập'
        self.fields['password'].label = 'Mật khẩu'
        self.fields['full_name'].label = 'Họ và tên'
        self.fields['email'].label = 'Email'
        self.fields['phone_number'].label = 'Số điện thoại'
        self.fields['address'].label = 'Địa chỉ'
class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone_number', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].label = "Họ và tên"
        self.fields['email'].label = "Email"
        self.fields['phone_number'].label = "Số điện thoại"
        self.fields['address'].label = "Địa chỉ"
class AvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].label = "Thay đổi ảnh đại diện"
class BillForm(forms.ModelForm):
    class Meta:
        model = ElectricityBill
        fields = [
            'bill_name', 'payment_date', 'consumption', 'unit_price', 'water_consumption', 
            'water_price', 'info_dien', 'info_nuoc', 'han_thanhtoan'
        ]

    def __init__(self, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)
        self.fields['bill_name'].label = "Tên Hóa Đơn"
        self.fields['payment_date'].label = "Ngày Tạo Hóa Đơn"
        self.fields['consumption'].label = "Lượng Điện Tiêu Thụ (kWh)"
        self.fields['unit_price'].label = "Giá Điện Mỗi Đơn Vị (VND)"
        self.fields['water_consumption'].label = "Lượng Nước Tiêu Thụ (m³)"
        self.fields['water_price'].label = "Giá Nước Mỗi Đơn Vị (VND)"
        self.fields['info_dien'].label = "Thông Tin Thêm Về Điện"
        self.fields['info_nuoc'].label = "Thông Tin Thêm Về Nước"
        self.fields['han_thanhtoan'].label = "Hạn Thanh Toán"

class BillSearchForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    CONSUMPTION_CHOICES = [
        ('<10', '<10 kWh'),
        ('10-30', '10 - 30 kWh'),
        ('30-100', '30 - 100 kWh'),
        ('100-200', '100 - 200 kWh'),
        ('>=200', '>= 200 kWh'),
    ]
    WATER_CONSUMPTION_CHOICES = [
        ('<10', '<10 m³'),
        ('10-30', '10 - 30 m³'),
        ('30-50', '30 - 50 m³'),
        ('>=50', '>= 50 m³'),
    ]

    month = forms.ChoiceField(choices=MONTH_CHOICES, required=False, label='Tháng')
    year = forms.CharField(max_length=4, required=False, label='Năm')
    consumption = forms.ChoiceField(choices=CONSUMPTION_CHOICES, required=False, label='Số lượng tiêu thụ điện')
    water_consumption = forms.ChoiceField(choices=WATER_CONSUMPTION_CHOICES, required=False, label='Số lượng tiêu thụ nước')

class PeriodSelectForm(forms.Form):
    PERIOD_CHOICES = (
        ('monthly', 'Tháng'),
        ('quarterly', 'Quý'),
        ('yearly', 'Năm'),
    )
    period = forms.ChoiceField(choices=PERIOD_CHOICES, label="Chọn kỳ thời gian")