const wrapper=document.querySelector('.wrapper'),
      inputPart=document.querySelector('.input-part'),
      infoTxt=document.querySelector('.info-txt'),
      locationBtn = inputPart.querySelector('button')
let inputField=document.querySelector('input');
let wIcon=document.querySelector('.weather-part img');
const arrowBack=wrapper.querySelector('header i');
const apiKey=`8aa70a82a835142c857a9a0fafbda30e`;
let api;

inputField.addEventListener('keyup',(e)=>{
    if(e.key=='Enter' && inputField.value!=''){
        requestApi(inputField.value);
    }
})

function requestApi(city){
    // console.log(city);
    api=`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${apiKey}`;
    fetchData();
    
}

locationBtn.addEventListener('click',()=>{

    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(onSuccess,onError);
    }
    else{
        alert('Sizning brouzeringiz geolokatsiyani qo\'llab quvatlamaydi')
    }
})

function onSuccess(position){
    // console.log(position)
    const{latitude,longitude} = position.coords;
    console.log(latitude,longitude)
    api=`https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&units=metric&appid=${apiKey}`;
    fetchData()
}
function onError(error){
    infoTxt.innerText = 'Siz Geolokatsiyaga roziliki bermadingiz';
    infoTxt.classList.add('error')
}


function fetchData(){
    infoTxt.innerText='Ob-xavo ma\'lumoti olinmoqda...';
    infoTxt.classList.add('pending');
    fetch(api)
    .then(response=>response.json())
    .then(data=>weatherDetail(data));

}
function weatherDetail(info){
    infoTxt.classList.replace('pending','error');
    console.log(info);
    if(info.cod=='404'){
        infoTxt.innerText='Bunday shahar mavjud emas';
    }else{
        const city=info.name;
        const country=info.sys.country;
        const {description,id}=info.weather[0];
        const {feels_like,humidity,temp}=info.main;

        // weater status 
        if(id==800){
            wIcon.src='static/icons/clear.svg';
        }else if(id==200 && id<=232){
            wIcon.src='static/icons/strom.svg';
        }else if(id==600 && id<=622){
            wIcon.src='static/icons/snow.svg';
        }else if(id==701 && id<=781){
            wIcon.src='static/icons/haze.svg';
        }else if(id==801 && id<=804){
            wIcon.src='static/icons/cloud.svg';
        }else if((id==300 && id<=321)|| id>=500 && id<=531){
            wIcon.src='static/icons/rain.svg';
        }else{
            wIcon.src='static/icons/clear.svg';
        }

        wrapper.querySelector('.temp .numb').innerText=Math.floor(temp);
        wrapper.querySelector('.weather').innerText=description;
        wrapper.querySelector('.location span').innerText=`${city},${country}`;
        wrapper.querySelector('.temp .numb-2').innerText=Math.floor(feels_like);
        wrapper.querySelector('.humidity span').innerText=`${humidity}%`;


        inputField.value='';
        infoTxt.classList.remove('pending','error');
        wrapper.classList.add('active');
    }

}
arrowBack.addEventListener('click',()=>{
    wrapper.classList.remove('active');
})