onSubmitSignUp = () => {
    let formData = new FormData();
    formData.append('username', this.state.username);
    formData.append('email', this.state.email);
    formData.append('password', this.state.password);

    fetch('http://127.0.0.1:8000/register/', {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: formData
        })
        .then(response => response.json())
        .then(user => {
            if (user) {
                console.log(user);
            } else {
                console.log("error");
            }
        })
}