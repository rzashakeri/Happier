const validation = new JustValidate('#signup_form');

validation
    .addField('#id_username', [
        {
            rule: 'minLength',
            value: 5,
        },
        {
            rule: 'maxLength',
            value: 150,
        },
        {
            rule: 'required',
            errorMessage: 'Username is required',
        },
    ])
    .addField('#id_email', [
        {
            rule: 'required',
            errorMessage: 'Email is required',
        },
        {
            rule: 'email',
            errorMessage: 'Email is invalid!',
        },
    ])
    .addField('#id_password1', [
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