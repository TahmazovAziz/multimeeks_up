const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');
const episode = document.getElementsByClassName('episode');

let corent_episode  = 0;
episode[0].style.display = 'block';
function ShowCurrentEpisode(){
    for(let i = 0; i < episode.length; i++){
        episode[i].style.display = 'none';
    }
    
    episode[corent_episode].style.display = 'block';
}

prevButton.addEventListener('click',()=>{
    if(corent_episode > 0){
        corent_episode--;
        ShowCurrentEpisode();
        console.log('ss')
    }
}); 
nextButton.addEventListener('click',()=>{
    if(corent_episode < episode.length - 1){
        corent_episode++;
        ShowCurrentEpisode();
        console.log('ss')

    }

})