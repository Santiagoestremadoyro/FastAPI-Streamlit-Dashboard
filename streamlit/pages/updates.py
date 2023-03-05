import streamlit as st

st.sidebar.success("Select an option above 👆🏼 ")



st.markdown("***")
st.markdown(
        '''
                # **Incoming updates!**
        '''
)

st.markdown("***")


st.markdown(
        '''
           Although this may be my first programming job, I have poured my heart and soul into designing a dashboard that stands the test of time. With a commitment to excellence and a passion for penguins, I vow to continually enhance this dashboard with valuable information and innovative features that will delight its users for years to come. Soon it will be integrated as a new feature to this dashboard:
        '''
    )

st.subheader("Flipper and bill length")
st.image('./data/flipper-bill.png')

st.subheader("Bill Length")
st.image('./data/bill-length.png')



st.header(":mailbox: Get In Touch With Me!")
st.markdown(
        '''
           Do you want to propose us ideas or contribute in some way to our community?
           Send us an email with your proposals/ideas and we will reply to you as soon as possible.
        '''
    )

contact_form = """
<form action="https://formsubmit.co/little.big.whales@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""


st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")