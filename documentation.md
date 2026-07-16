# Documentation 

## Paper Summary

For our Replication Assignment we chose to implement the Concept of "Text Entry Using a Dual Joystick Game Controller" by Andrew D. Wilson and Maneesh Agrawala first published at CHI in 2006.

Their work proposes a text input method that uses both analog joysticks of a game controller simultaneously, instead of only one, which was common at the time of publishing.

The idea is to divide the keyboard into a left and a right half. The left joystick controlls the left half, while the right joystick controls the right. This design mimics a two-handed typing style used on standard keyboards, allowing users to utilize existing typing habits. Next to joystick controls, the system uses the trigger keys to enter selected characters of the corresponding joystick (i.e. left trigger enters selected key on the left half)

In addition to increased text entry speed, the authors point out that, firstly, the familiar keyboard layout reduces the learning effort in comparison to alternative custom layouts, and secondly, their method requires no additional devices, as it relies only on the analog joysticks already available on standard game controllers.

Their method intends to make text entry for online chats and general console usage more efficient and comfortable.


## Implementation

We figured that Wilson and Agrawalas method can be implemented using a similar approach we previously covered in this course, using Pynput to handle joystick and button inputs and Pyglet as graphics interface.

!! TODO: !!

#### Keyboard overlay

Our keyboard overlay is placed centered at the bottom of the screen, highlighting the currently selected characters and displaying information about the controls.

Using pyglet, we extract the users screen dimensions and display a pyglet interface centered at the bottom (keyboard_view.py).
The keyboards characters are implemented as Arrays, allowing to iterate through them when handling the joystick input (i.e. either row left/right or column up/down)


#### Input handler
... 


## Other Papers

In addition to the paper we chose to implement, we also considered other works. While they raised our interest, they were not quite fitting for the scope of this assignment or, in case of the "Bubble Cursor", not available anymore. 

### The Bubble Cursor

The paper "The bubble cursor: enhancing target acquisition by dynamic resizing of the cursor's activation area" introduces the Bubble Cursor, a pointing technique that is designed to improve target selection in user interfaces. Unlike a regular cursor, which has a single point for selection, the Bubble Cursor uses a dynamically resizing circle ("bubble"). Moving the cursor automatically expands or shrinks the bubble, so that it always selects exactly one target, which is the nearest selectable object.

Its goals are to improve target selection speed and reducing pointing errors, while still maintaining the same visual appearance as a regular cursor, offering support especially on dense interfaces.

Considering the rather simple implementation and the fact that no additional peripherals are needed to realize this idea, it would be very fitting for this assignment. However, as mentioned, it was no longer available.


!! TODO: noch ein paper !!