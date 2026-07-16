# Documentation 

## Paper Summary

For our Replication Assignment we chose to implement the Concept of "Text Entry Using a Dual Joystick Game Controller" by Andrew D. Wilson and Maneesh Agrawala first published at CHI in 2006.

Their work proposes a text input method that uses both analog joysticks of a game controller simultaneously, instead of only one, which was common at the time of publishing.

The idea is to divide the keyboard into a left and a right half. The left joystick controlls the left half, while the right joystick controls the right. This design mimics a two-handed typing style used on standard keyboards, allowing users to utilize existing typing habits. Next to joystick controls, the system uses the trigger keys to enter selected characters of the corresponding joystick (i.e. left trigger enters selected key on the left half)

In addition to increased text entry speed, the authors point out that, firstly, the familiar keyboard layout reduces the learning effort in comparison to alternative custom layouts, and secondly, their method requires no additional devices, as it relies only on the analog joysticks already available on standard game controllers.

Their method intends to make text entry for online chats and general console usage more efficient and comfortable.

To test out whether their method actually achieves these goals, the authors conducted a user study with 14 participants who had varying experience using computers but no regular use of game controllers. The trial consisted of a subject reproducing a displayed phrase using four different onscreen keyboards. The keyboards featured 2 different layouts (alphabetical and standard QWERTY) and two types of controls (single and dual sticks).

The best results amongst all four, with a Words-per-minute rate of 7.08, was achieved by with dual-stick QWERTY version. For both layouts, the dual-stick versions scored a higher typing speed than the single-stick input, demonstrating the superiority of the authors' method over the standard.


## Implementation

We figured that Wilson and Agrawalas method can be implemented using a similar approach we previously covered in this course, using Pynput to handle joystick and button inputs and Pyglet as graphics interface.

Following the user studies results, we chose to implement the standard QWERTY layout, as it is the more familiar variant for most users and it has been proven to yield the highest typing speed.

### Keyboard overlay

Our keyboard overlay is placed centered at the bottom of the screen, highlighting the currently selected characters and displaying information about the controls.

Using pyglet, we extract the users screen dimensions and display a pyglet interface centered at the bottom (keyboard_view.py).

The keyboards characters are implemented as arrays, allowing to iterate through them when handling the joystick input (i.e. either row left/right or column up/down)


### Input handler

Our input handler uses pynput to handle three different types of events, those being joystick movement, button press and trigger press.

The Joystick movement is used to navigate the selection box to a preferred character. Additionally users can delete the last character(backspace) by pointing both sticks to the left.
Pointing both sticks upwards selects the 'special' keyboard overlay, providing more special characters like brackets and symbols. 

Button presses are used to manipulate the overlay. Pressing "X" allows a user to toggle the overlay, while pressing "B" closes it (program stop). Pushing in either joystick also counts as button press, changing the input to capital letters.

The trigger buttons are used to enter selected characters on the corresponding side. Additionally, pressing both trigger buttons simultaneously enters a space.

### Operating Systems

We recommend using either Windows or Linux as operating systems, as they have been thoroughly tested during implementation.

We had no option to additionally test our implementation on MacOS yet, so it might not work as expected.

### Controls Overview

| Action | Control | Description |
| :--- | :--- | :--- |
| **Navigate Left** | <kbd>L-Stick</kbd> | Navigate the left character selection. |
| **Navigate Right** | <kbd>R-Stick</kbd> | Navigate the right character selection. |
| **Enter Left** | <kbd>LB</kbd> | Enter the selected left character. |
| **Enter Right** | <kbd>RB</kbd> | Enter the selected right character. |
| **Space** | <kbd>L3</kbd> and <kbd>R3</kbd> | Enter a space. |
| **Backspace** | <kbd>L-Stick ←</kbd> and <kbd>R-Stick ← </kbd> | Backspace (delete last character). |
| **Capital Letters** | <kbd>L3</kbd> or <kbd>R3</kbd> | Switch to capital letters. |
| **Special Keyboard** | <kbd>L-Stick ↑</kbd> and <kbd>R-Stick ↑</kbd> | Switch to special Keyboard. |
| **Toggle Overlay** | <kbd>X</kbd> | Toggle keyboard overlay. |
| **Stop Program** | <kbd>B</kbd> | Stop the Program. |

## Other Papers

In addition to the paper we chose to implement, we also considered other works. While they raised our interest, they were not quite fitting for the scope of this assignment or, in case of the "Bubble Cursor", not available anymore. 

### EdgeWrite

Wobbrock et al's work in "EdgeWrite: a stylus-based text entry method designed for high accuracy and stability of motion" would have been a very fitting topic, since we already covered the "$1 Unistroke Recognizer" in this course.

Their concept features a unistroke gesture alphabet that is intended to be written with a stylus inside a square input area with physical edges. The key idea is that the stylus is guided by the edges, which provides physical support and reduces unintended movements.

Each character is recognized not by exact shape, but the sequence of corners the stylus touches while tracing a gesture. Because only the visited corners determine a character, it is tolerant of shaky or imprecise movements.

Their goals are to improve text entry accuracy, increase motion stability and provide a supportive design especially for people with motor impairments that struggle with common drawing gesture text entry methods.

In the publication the authors mention specific hardware, in their case a touchpad with physical template and a stylus for drawing gestures. As we do not have access to similar devices, we could not implement this work in the same way and decided to select a different topic.

### The Bubble Cursor

The paper "The bubble cursor: enhancing target acquisition by dynamic resizing of the cursor's activation area" introduces the Bubble Cursor, a pointing technique that is designed to improve target selection in user interfaces. Unlike a regular cursor, which has a single point for selection, the Bubble Cursor uses a dynamically resizing circle ("bubble"). Moving the cursor automatically expands or shrinks the bubble, so that it always selects exactly one target, which is the nearest selectable object.

Its goals are to improve target selection speed and reducing pointing errors, while still maintaining the same visual appearance as a regular cursor, offering support especially on dense interfaces.

Considering the rather simple implementation and the fact that no additional peripherals are needed to realize this idea, it would be very fitting for this assignment. However, as mentioned, it was no longer available.
