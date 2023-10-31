# hand_gesture_socket_test
Hand Gestures recognition app - mainly used for sending packages / testing UDP sockets with this repo here: https://github.com/yuurichan/hand_gesture_socket_test_unity

EDIT:
This is a heavily modified version of https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe AND https://github.com/kinivi/hand-gesture-recognition-mediapipe. Including:
- Different dataset + gestures.
- Removed keypoint detection.
- Removed hand landmarks logging (to CSV file).
- Modified mainly for sending gesture labels (string) data using UDP Socket.
- Can be built as a seperate app using pyinstaller.
- Is (somewhat) integrated with https://github.com/Ghostexvan/Project001. Can be used as a game controller for said project.

