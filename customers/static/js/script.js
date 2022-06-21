const imgDiv = document.querySelector('.profile-pic-div');
const img = document.querySelector('#image');
const file = document.querySelector('#photo');
const uploadBtn = document.querySelector('#uploadBtn');

const imgDiv2 = document.querySelector('.profile-pic-div2');
const img2 = document.querySelector('#sign_image');
const file2 = document.querySelector('#sign');
const uploadBtn2 = document.querySelector('#uploadBtn2');

//if user hover on img div 

imgDiv.addEventListener('mouseenter', function(){
    uploadBtn.style.display = "block";
});

imgDiv2.addEventListener('mouseenter', function(){
    uploadBtn2.style.display = "block";
});


//if we hover out from img div

imgDiv.addEventListener('mouseleave', function(){
    uploadBtn.style.display = "none";
});

imgDiv2.addEventListener('mouseleave', function(){
    uploadBtn2.style.display = "none";
});

//lets work for image showing functionality when we choose an image to upload

//when we choose a foto to upload

photo.addEventListener('change', function(){
    //this refers to file
    const choosedFile = this.files[0];

    if (choosedFile) {

        const reader = new FileReader(); //FileReader is a predefined function of JS

        reader.addEventListener('load', function(){
            img.setAttribute('src', reader.result);
        });

        reader.readAsDataURL(choosedFile);

        //Allright is done

        //please like the video
        //comment if have any issue related to vide & also rate my work in comment section

        //And aslo please subscribe for more tutorial like this

        //thanks for watching
    }
});


file2.addEventListener('change', function(){
    //this refers to file
    const choosedFile = this.files[0];

    if (choosedFile) {

        const reader = new FileReader(); //FileReader is a predefined function of JS

        reader.addEventListener('load', function(){
            img2.setAttribute('src', reader.result);
        });

        reader.readAsDataURL(choosedFile);

        //Allright is done

        //please like the video
        //comment if have any issue related to vide & also rate my work in comment section

        //And aslo please subscribe for more tutorial like this

        //thanks for watching
    }
});