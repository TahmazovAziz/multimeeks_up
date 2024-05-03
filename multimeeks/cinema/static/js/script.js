const prevButton = document.getElementById('next');
const nextButton = document.getElementById('prev');
const episode = document.getElementsByClassName('episode');
const count = document.getElementById('count')
const roomName = JSON.parse(document.getElementById('room-name').textContent);

let corent_episode  = 0;

episode[0].style.display = 'block';

console.log(episode.length);
if(episode.length < 2){
    prevButton.style.display ='none'
    nextButton.style.display ='none'
    count.style.display ='none'
}
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
    }
}); 
nextButton.addEventListener('click',()=>{
    if(corent_episode < episode.length - 1){
        corent_episode++;
        ShowCurrentEpisode();

    }

})


const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-text').innerHTML += ('<b style="color:green">'+data.niknaim+'</b>' +':'+data.message + '<br>');
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};



document.querySelector('#chat-message-input-2').focus();
document.querySelector('#chat-message-input-2').onkeyup = function(e) {
    if (e.key === 'Enter') {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};



document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const messageInputDom2 = document.querySelector('#chat-message-input-2');
    const message = messageInputDom.value;
    const niknaim = messageInputDom2.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        'niknaim': niknaim
    }));
    messageInputDom2.value = '';
    messageInputDom.value = '';
};