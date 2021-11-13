document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("user").addEventListener('change', validateUser); 
  });

const validateUser = async ()=>{
        try{
            const baseURL = "http://127.0.0.1:4500/api/"
            const id=document.getElementById("user").value
            const form = document.getElementById("form_add_bill")
            const messageInvalid = document.getElementById('invalidMessage')
            const messagevalid = document.getElementById('validMessage')
            const user = await (await fetch(`${baseURL}customer/${id}`,{})).json()
            const submitButton = document.getElementById('submitButton')
            if(!user.code){
                submitButton.disabled=true
                messagevalid.style.display='none'
                messageInvalid.style.display='block'
            }else{
                submitButton.disabled=false
                messagevalid.style.display='block'
                messageInvalid.style.display='none'
            }
        }catch(e){
            console.error(e)
        }
}


