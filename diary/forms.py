from django import forms


class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前',max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル',max_length=30)
    massage = forms.CharField(label='メッセージ',widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        # self.fields['name'].widget.attrs['class']='form-control col-9'
        # self.fields['name'].widget.attrs['placeholder']='ここにお名前を入れてください'

        # self.fields['email'].widget.attrs['class']='form-control col-11'
        # self.fields['email'].widget.attrs['placeholder']='メールアドレスをここに入れてください'

        # self.fields['title'].widget.attrs['class']='form-control col-11'
        # self.fields['title'].widget.attrs['placeholder']='タイトルをここに入れてください'

        # self.fields['message'].widget.attrs['class']='form-control col-12'
        # self.fields['message'].widget.attrs['placeholder']='メッセージをここに入れてください'

