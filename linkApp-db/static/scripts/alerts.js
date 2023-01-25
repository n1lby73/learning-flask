function validateUsername() {
    const pattern = /^[a-zA-Z][a-zA-Z0-9_]{5,20}$/;
    if (!username.value.match(pattern)) {
        setError(username, "Username must start with a letter, contain only letters, numbers, and the underscore character, and be between 5 and 20 characters long.");
    }
}

const username = document.getElementById('username');
username.onblur = validateUsername;

const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

const form = document.getElementById('forms');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    validateInputs();

});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('If the element with the ID "form" exists in the HTMLsuccess')
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

const validateInputs = () => {
    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const password2Value = password2.value.trim();

    if(usernameValue === '') {

        setError(username, 'Username is required');

    }

    else if(emailValue === '') {
        setError(email, 'Email is required');

        if (!isValidEmail(emailValue)) {
            setError(email, 'Provide a valid email address');
        } else {
            setSuccess(email);
        }
    }

    else if(passwordValue === '') {
        setError(password, 'Password is required');

        if (passwordValue.length < 8 ) {
            setError(password, 'Password must be at least 8 character.')
        } else {
            setSuccess(password);
        }
    } 

    else if(password2Value === '') {
        setError(password2, 'Please confirm your password');

        if (password2Value !== passwordValue) {
            setError(password2, "Passwords doesn't match");
        } else {
            setSuccess(password2);
        }
    }

    else {

        var data = { 
            
            "username": usernameValue,
            "email": emailValue,
            "password":passwordValue,
            "password2":password2Value,
        
        };

        fetch('/login', {
            method: 'POST',
            body: JSON.stringify(data),
            headers: { 'Content-Type': 'application/json' }
        })
        .then(response => {
            if (response.ok){
                console.log(response.status);
                console.log("Request succeeded");
                return response.json();
            }

            else{

                console.log("error sending data");
            }
        })
        .then(data => {
            if (data.success === true){
                console.log("succ");
                window.location.replace('/success');
            }

            else{
                
                console.log(data);
                console.log("i won't redirect");
            }
        })
        .catch(error => console.error(error));

// How to check response and data using .then
// Response { type: "basic", url: "http://127.0.0.1:3565/login", redirected: false, status: 200, ok: true, statusText: "OK", headers: Headers(5), body: ReadableStream, bodyUsed: false } meanning
        // fetch('/login', {
        //     method: 'POST',
        //     body: JSON.stringify(data),
        //     headers: { 'Content-Type': 'application/json' }
        // }).then(response => {
        //     if(response.ok) {

        //         // if (data.success === true) {
        //         //     window.location.href = '/success';
        //         // } else {
        //         //     console.log("Error sending data");
        //         // }
        //         console.log(response.status)
        //         console.log("Request succeeded");
        //         // window.location.replace('login')
        //         // window.location.href='/login'
        //         // return response.json();
        //     }else{
        //         console.log(response.status)
        //         throw new Error('Error: ' + response.status);
        //     }
        // }).then(data => {

        //     if (data.success === true) {
        //             console.log("true")
        //             window.location.href = '/success';
        //         } else {
        //             console.log("Error sending data");
        //         }

        // }).catch(error => {
        //     console.error(error);
        // });
        
        
        // fetch('/login',
        // {

        //     method: 'POST',
        //     body: JSON.stringify(data),
        //     headers: { 'Content-Type': 'application/json' }
            
        // }
        // ).then(response => {
        //         console.log(response.status)
        //         if (response.ok) {
        //             // return response.json();
        //             // console.log(response.status)
        //             console.log("Request succeeded");
        //             window.location.href='/login'
        //         } 
                
        //         else {
        //             console.log("Request failed");
        //         }
        //     })
            
        //     .catch(error => console.error('Error:', error));

        // console.log("reached here");
    }
};