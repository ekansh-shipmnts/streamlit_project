from streamlit_webrtc import webrtc_streamer,WebRtcMode, RTCConfiguration
RTC_CONFIGURATION = RTCConfiguration(
        {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})
webrtc_streamer(key="sample",rtc_configuration=RTC_CONFIGURATION,mode=WebRtcMode.SENDRECV,media_stream_constraints={"video": True, "audio": False},
        async_processing=True,)