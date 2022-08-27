        let moon = document.querySelector('.moon')
        let toggle = document.querySelector('.toggle')
        let darkd = document.querySelector('.darkd')
        toggle.addEventListener('click', () => {
        darkd.classList.toggle("darkd_activ")
        moon.classList.toggle('fas')
        })