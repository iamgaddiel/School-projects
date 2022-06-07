const messengers = document.querySelectorAll('span[class="chat-list"]');

messengers.forEach((messenger) => {
  messenger.addEventListener("click", (event) => {
    event.preventDefault();

    //todo: get value from messenger text input
    const friendId = messenger.getAttribute("data-id");
    const url = `${location.protocol}//${location.host}/chat/get_messages/${friendId}/`;
    const hiddenInput = document.querySelector("#friendId");
    let messageBox = document.querySelector(".box_messenger");

    //todo: get value from hidden input
    hiddenInput.setAttribute("value", friendId); 

    try {
      (async () => {
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
          messageBox.innerHTML = "";
        }
      })();
    } catch (err) {
      throw new Error("error fetching data", err);
    }
  });
});

const handleMessageForm = document.querySelector("#messangerForm");
handleMessageForm.addEventListener("submit", (event) => {
  event.preventDefault();
  let message = document.querySelector("#message").value;
  let friendId = document.querySelector("#friendId").value;


  console.log(message, friendId);
  fetch(`http://localhost:8000/chat/send_message/${message}/${friendId}`)
  .then((res) => res.json())
  .then(() => getChatMessage(friendId))
});

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
