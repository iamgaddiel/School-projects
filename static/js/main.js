const messenger = document.querySelectorAll('span[class="chat-list"]')
messenger.forEach((messenger) => {
  messenger.addEventListener("click", (event) => {
    event.preventDefault();

    //todo: get value from messenger text input
    const friendId = messenger.getAttribute("data-id");
    const url = `${location.protocol}//${location.host}/chat/get_messages/${friendId}/`;
    const hiddenInput = document.querySelector("#friendId");
    
    //todo: get value from hidden input
    hiddenInput.setAttribute("value", friendId); 
    
    try {
      (async () => {
        let messageBox = document.querySelector(".box_messenger");
        let messages = (await (await fetch(url)).json()).data;
        let messageBody = ``;
        messageBox.innerHTML = "";

        if (messages.length > 0) {
          messages.forEach((message) => {
            if (message._from_id == friendId) {
              console.log("left");
              messageBody = `
                <div class="single_message_chat">
                <div class="message_content_view red_border">
                  <p>
                    <span>${message.message}<br /></span>
                  </p>
                </div>
              </div>
                `;
            } else {
              messageBody = `
              <div class="single_message_chat sender_message">
                <div class="message_content_view">
                  <p>
                    <span>${message.message}<br /></span>
                  </p>
                </div>
              </div>
              `;
            }
            messageBox.innerHTML += messageBody;
          });
        } else {
          messageBox.innerHTML = "No messages found";
        }
      })();
    } catch (err) {
      throw new Error("error fetching data", err);
    }
  });
});


// Send individual message
const handleMessageForm = document.querySelector("#messangerForm");
handleMessageForm?.addEventListener("submit", (event) => {
  event.preventDefault();
  let message = document.querySelector("#message").value;
  let friendId = document.querySelector("#friendId").value;


  console.log(message, friendId);
  fetch(`http://localhost:8000/chat/send_message/${message}/${friendId}`)
  .then((res) => res.json())
  .then(() => getChatMessage(friendId))
});


// GEt individual Chat
const getChatMessage = async (friendId) => {
  // const friendId = messenger.getAttribute("data-id");
  const url = `${location.protocol}//${location.host}/chat/get_messages/${friendId}/`;
  const messages = (await (await fetch(url)).json()).data;
  const messageBox = document.querySelector(".box_messenger");
  let messageBody = ``;
  messageBox.innerHTML = "";

  if (messages.length > 0) {
    messages.forEach((message) => {
      if (message._from_id == friendId) {
        messageBody = `
          <div class="single_message_chat">
          <div class="message_content_view red_border">
            <p>
              <span>${message.message}<br /></span>
            </p>
          </div>
        </div>
          `;
      }
      else {
        messageBody = `
        <div class="single_message_chat sender_message">
          <div class="message_content_view">
            <p>
              <span>${message.message}<br /></span>
            </p>
          </div>
        </div>
        `;
      }
      messageBox.innerHTML += messageBody;
    });
  }
  else {
    messageBox.innerHTML = "";
  }
};


// -------------------------------------- [ Group Chat ] ---------------------
// GET GROUP MESSAGE
const group = document.querySelectorAll('span[class="group-list"]').forEach(group => {
  group.addEventListener('click', (event) => {

    //todo: get value from messenger text input
    const groupId = group.getAttribute("data-id");
    const url = `${location.protocol}//${location.host}/chat/group_messages/${groupId}/`;
    const hiddenInput = document.querySelector("#groupId");
    const userId = document.querySelector("#userId").getAttribute('value')
    
    //todo: get value from hidden input
    hiddenInput.setAttribute("value", groupId); 
    
    try {
      //  get group messages
      (async () => {
        let messageBox = document.querySelector(".box_messenger");
        let messages = (await (await fetch(url)).json()).data;
        let messageBody = ``;
        messageBox.innerHTML = "";

        if (messages.length > 0) {
          messages.forEach((message) => {
            if (message._from_id != userId) {
              messageBody = `
                <div class="single_message_chat">
                <div class="message_content_view red_border">
                  <p>
                    <span>${message.message}<br /></span>
                  </p>
                </div>
              </div>
                `;
            } else {
              messageBody = `
              <div class="single_message_chat sender_message">
                <div class="message_content_view">
                  <p>
                    <span>${message.message}<br /></span>
                  </p>
                </div>
              </div>
              `;
            }
            messageBox.innerHTML += messageBody;
          });
        } else {
          messageBox.innerHTML = "No messages found";
        }
      })();
    } catch (err) {
      throw new Error("error fetching data", err);
    }
  })
})


// Send group Messuage
const handleGroupMessageForm = document.querySelector("#groupMessengerForm");
handleGroupMessageForm?.addEventListener("submit", (event) => {
  event.preventDefault();
  let message = document.querySelector("#message").value;
  let groupId = document.querySelector("#groupId").value;


  fetch(`http://localhost:8000/chat/send_group_message/${message}/${groupId}`)
  .then((res) => res.json())
  .then(() => getGroupChatMessage(groupId))
});


// GEt group Chat
const getGroupChatMessage = async (groupId) => {
  const url = `${location.protocol}//${location.host}/chat/group_messages/${groupId}/`;
  const messages = (await (await fetch(url)).json()).data;
  const messageBox = document.querySelector(".box_messenger");
  const userId = document.querySelector("#userId").getAttribute('value')

  let messageBody = ``;
  messageBox.innerHTML = "";

  if (messages.length > 0) {
    messages.forEach((message) => {
      if (message._from_id != userId) {
        messageBody = `
          <div class="single_message_chat">
          <div class="message_content_view red_border">
            <p>
              <span>${message.message}<br /></span>
            </p>
          </div>
        </div>
          `;
      }
      else {
        messageBody = `
        <div class="single_message_chat sender_message">
          <div class="message_content_view">
            <p>
              <span>${message.message}<br /></span>
            </p>
          </div>
        </div>
        `;
      }
      messageBox.innerHTML += messageBody;
    });
  }
  else {
    messageBox.innerHTML = "";
  }
};

