fetch('https://jsonplaceholder.typicode.com/users')
.then(res=>res.json())
.then(data=>{
    const ul=document.querySelector('ul');
    data.forEach(user => {
        const li=document.createElement("li");
        li.textContent=user
        ul.appendChild(li)
  
    });
})
.catch(err=>{console.error("Error",err)});