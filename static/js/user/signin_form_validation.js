const validation = new JustValidate('#signin_form');

validation
    .addField('#id_login', [
        {
            rule: 'required',
            errorMessage: 'username or email is required',
        },
    ])
    .addField('#id_password', [
        {
            rule: 'customRegexp',
            value: /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*#?&^_-]).{8,}/,
            errorMessage: " Minimum eight characters, at least one uppercase letter , one lowercase letter , one number , one special character "
        },
        {
            rule: 'required',
            errorMessage: 'Password is required',
        }
    ])
    .onSuccess((event) => {
        validation.form.submit();
    });