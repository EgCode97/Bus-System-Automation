const userAction = async () => {
    const response = await fetch('http://127.0.0.1:8000/api', {
      //mode: 'no-cors',
      method: 'GET',
      //body: myBody, // string or object
      headers: {
        'Content-Type': 'application/json'
      }
    });
    //const myJson = await response.json(); //extract JSON from the http response
    // do something with myJson

    console.log(response)
  }