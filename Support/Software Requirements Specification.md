# Software Requirements Specification (Draft)

Revision History:

| Date | Author | Description |
| ---- | ------ | ----------- |
| Apr 5 | Xiaoquan Xu | Add use cases |

## Use Cases

- Case: User Register 注册
- Case: User Login 登录
- Case: User record the motion and upload data 记录上传
- Case: add a new device to the system 添加设备
- Case: Reset the model 重置
- Case: Show prediction result 显示预测结果
- Case: View the status of model 显示模型状态
- Case: Get training motion data 获取训练数据
- Case: Save the pretrained model checkpoint 
- Case: personalized fine-tuned model checkpoints
- Case: user information 用户信息
- Case: algorithm model 算法模型
- Case: Motion data of sensors
- Case: Store the prediction result
- Case: Algorithm Output prediction results
- Case: Get the pretrained model
- Case: Fine-tune the model
- Case: Predict the result
- Case: Select the algorithm
- Case: Application wants the prediction of motions
- Case: Application wants an adjustable network structure
- Case: User Wants to Register
- Case: User Wants to Login
- Case: User Wants to View The Status of The System
- Case: User Wants to Add a New Device to The System
- Case: User wants to start record motions
- Case: User wants to upload/discard the data
- Case: User wants to individualize the model
- Case: User wants to reset the model
- Case: Register a New Account
- Case: Log in to the Application
- Case: View User Information
- Case: Add Equipment
- Case: Check the Status of the Equipment
- Case: View Equipment Details
- Case: View Usage Guide
- Case: Start to Collect Data
- Case: Upload the Collected Data
- Case: Discard the Collected Data
- Case: Interaction wants to store user personal information in the database
- Case: Interaction wants to use user personal information to login in the database
- Case: Interaction wants to change user personal information in the database
- Case: Algorithm Wants to Save the Algorithm model in Binary form
- Case: Algorithm Wants to Save Relevant Datasets
- Case: Algorithm Wants to Save the Results of trained sensor data
- Case: Algorithm Wants to Save the performance metrics of the Algorithm model
- Case: Calling API for register and login
- Case: Calling API for changing information
- Case: Upload and download sensor data.
- Case: Upload and download the trained model

### Case: Example

- Version: 1
- Created: 
- Authors: 
- Source: 
- Actors: 
- Goal: 
- Summary: 
- Trigger: 
- Frequency: 
- Precondition: 
- Postconditions: 

![]()

#### Basic Flow

| Actor | System |
| ----- | ------ |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

### Case: User Register

- Version: 1
- Created: Apr 1
- Authors: Wenhui ZHOU
- Source: Server
- Actors: Add a user to the system
- Goal: To make user register in the system
- Summary: This requirement allows new user to join the system and use the system to upload motion data and predict motion.
- Trigger: When new users want to join in the system
- Frequency: Decided by number of new users
- Precondition: The system permit adding new user
- Postconditions: The interface has verified the two inputs of password are the same

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5401.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| New User registers in system |  |
|  | Check the user account is unique |
|  | Check the password is consistent with the regulation |
|  | Create user account and add to the database |
|  | Return success information to the Interface |
| Interface show success information |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| User account has existed |  |
|  | Return information of user account repetition |
| User password is not consistent with regulation |  |
|  | Return information of password format error |

### Case: User Login

- Version: 1
- Created: Apr 1
- Authors: Wenhui ZHOU
- Source: Server
- Actors: Verify user login
- Goal: To make User login in the system
- Summary: This requirement allow user to log in the system and use other function.
- Trigger: When new user log in
- Frequency: often
- Precondition: The system is running 
- Postconditions: The database has user information

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5403.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Interface transmit user login request |  |
|  | Get user information from database |
|  | Check user account exists |
|  | Check password is correct |
|  | Set user state and return success |
| Interface show user system interface |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| User account not exists |  |
|  | Return information of account not exists |
| Password is not correct |  |
|  | Return information for user to check the password |

### Case: User record the motion and upload data

- Version: 1
- Created: Apr 1
- Authors: Wenhui ZHOU
- Source: Server
- Actors: Record motion data and upload
- Goal: To permit user to upload own motion data
- Summary: This requirement allows user to upload motion data for training and prediction
- Trigger: When user use device to record data
- Frequency: often
- Precondition: The device is connected to the system and the user login
- Postconditions: The device is connected to the system and the user login

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba540b.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Device transmit the real-time data |  |
|  | Store the data temporarily when the device is transmitting |
|  | Reformat the motion data |
|  | Add data to the database |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| Interface upload data file |  |
|  | Get the datafile and read data from it |
|  | Reformat the data |
|  | Add data to database |

### Case: add a new device to the system

- Version: 1
- Created: Apr 1
- Authors: Wenhui ZHOU
- Source: Server
- Actors: Add a new device
- Goal: To permit user to connect new device to get data
- Summary: This requirement allows user s to add new devices to the system
- Trigger: When user wants to add a new device to get data 
- Frequency: seldom
- Precondition: The interface allows to connect to a new device
- Postconditions: The device is ready

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba540c.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Interface transmit information of a new device |  |
|  | Analyze the device information and request for device status |
|  | Try to connect to the device |
|  | Record the device in the system and return success |
| Interface show device on the interface |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| Fail to connect to the device  |  |
|  | Retry for several times |
|  | Return error information |

### Case: Reset the model

- Version: 1
- Created: Apr 1
- Authors: Wenhui ZHOU
- Source: Server
- Actors: Clear the information of model belonging to user
- Goal: To clear the model information of users
- Summary: This requirement is used to permit user to reset his or her own model and running a new model to predict. It will delete relating information in the database.
- Trigger: When user choose reset the model on the interface
- Frequency: Seldom
- Precondition: The interface offer reset button
- Postconditions: The database of model information can be modified

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba540f.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Interface transmit reset request |  |
|  | Verify the user identity |
|  | Request the database to delete the model information of this user |
|  | Response to the interface that the model has been reset |
| Interface show success information to the user |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| Interface transmit reset request |  |
|  | Verify the user identity |
|  | Database find no relating model information of this user |
|  | Response to the interface that reset fail since no model exists |
| Interface show failure information |  |

### Case: Show prediction result

- Version: 1
- Created: Apr 1
- Authors: Wenhui ZHOU
- Source: Server
- Actors: Show prediction result
- Goal: To get result from Algorithm after running 
- Summary: This requirement allows to show the result on the interface
- Trigger: When algorithm successfully generate prediction result
- Frequency: often
- Precondition: often
- Postconditions: None

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5412.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Algorithm transmit the result |  |
|  | Get the result and reformat the result information |
|  | Transmit the result information to the interface |
| Interface show the result information |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| No result transmits from algorithm |  |
|  | Return waiting information to interface |

### Case: View the status of model

- Version: 1
- Created: Apr 1
- Authors: Wenhui ZHOU
- Source: Server
- Actors: Show the system status to the user
- Goal: To check the status of system
- Summary: This requirement allow user to view the status of the system now and decide whether to upload data and predict.
- Trigger: When user request to view the status
- Frequency: seldom
- Precondition: The system is running
- Postconditions: none

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5416.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Interface transmit request of view status |  |
|  | Get status of each section of the system |
|  | Integrate the system status information |
|  | Return the information to interface |
| Interface show status information to the user |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| The system status is forbidden to view |  |
|  | Return information of no permission |

### Case: Get training motion data

- Version: 1
- Created: Apr 2
- Authors: Cong HUA
- Source: Algorithm
- Actors: Algorithm
- Goal: get training motion data
- Summary: Algorithm developers need to load the training data to train the model from scratch. We will return the training motion data to respond to requests
- Trigger: Input the number of expected training data samples and the name of dataset
- Frequency: To be determined
- Precondition: Have built the framework and designed the dataloader
- Postconditions: No

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5418.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Algorithm-input<the number of expected training data samples, the name of dataset> |  |
|  | Receive the number and the dataset name |
|  | Determine if this demand number in specified dataset is reasonable |
|  | Fetch dataset from the database |
|  | Return the specified dataset or warning |
| Algorithm-receive < expected training dataset> |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
    
### Case: Save the pretrained model checkpoint

- Version: 1
- Created: Apr 2
- Authors: Cong HUA
- Source: Server
- Actors: Algorithm
- Goal: Save the pretrained model checkpoint
- Summary: When algorithm developers have trained the model successfully, they will save the pretrained model checkpoint into the database
- Trigger: Input the pretrained model checkpoints
- Frequency: To be determined 
- Precondition: Algorithm developers have trained the model successfully
- Postconditions: No

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba541a.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Algorithm input pretrained model checkpoints |  |
|  | Recevie the checkpoint |
|  | Check the disk space  |
|  | Save the checkpoints into the database  |
|  | Return success |
| Algorithm receive checkpoints- successfully-created-confirmation |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

### Case: personalized fine-tuned model checkpoints

- Version: 1
- Created: Apr 2
- Authors: Cong HUA
- Source: Server
- Actors: Algorithm
- Goal: personalized fine-tuned model checkpoints
- Summary: Based on pretrained model  and personalized  features,  fine tune the model and save the personalized model checkpoint into the database
- Trigger: Input name
- Frequency: To be determined 
- Precondition: Interface have uploaded the personalized data, and personalized data has been stored in database
- Postconditions: No

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba541e.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Algorithm input person name |  |
|  | Algorithm input person name |
|  | Check that if name exists |
|  | Return model checkpoint and personalized data |
| Algorithm receive the model parametrs and personalized data |  |
| Algorithm input fine-tuned personalized model checkpoint |  |
|  | Receive the personalized model checkpoints |
|  | Save  the checkpoint into the database |
|  | Return success |
| Algorithm receive the personalized-model-successfully-save |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

### Case: user information

- Version: 1
- Created: Mar 31
- Authors: Wenxuan ZHU
- Source: User account information
- Actors: Read, store, modify and delete
- Goal: User information can be read, stored, modified and deleted
- Summary: User information can be read, stored, modified and deleted
- Trigger: User login system
- Frequency: Every time user log in
- Precondition: Database save complete user information
- Postconditions: Users can access data in the database

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5422.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Guset input account and password |  |
|  | Receive account and password |
|  | Verify account and password |
|  | Create user |
|  | Return login sucess |
| Guest receive user information |  |
| Successfully log in |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| Guest input wrong account or password  |  |
|  | Verify account and password |
|  | Find exception |
| Guest receive exception |  |
| Failed to login |  |

### Case: algorithm model

- Version: 1
- Created: Mar 30
- Authors: Wenxuan ZHU
- Source: Store the algorithm model for use
- Actors: Store, modify and read
- Goal: Store, modify and read algorithm models
- Summary: Store the binary file of the algorithm model in the database so that it can be read and used
- Trigger: Data need to be predicted
- Frequency: Every time predict
- Precondition: The model is stored in the database or the model has already been trained
- Postconditions: Model data can be read

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5426.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Guest input model data |  |
|  | Guest input model data |
|  | Verify model data |
|  | store model data  |
| Guest receive model data |  |
| Successfully store data |  |
| Guest input model read request |  |
|  | Verify request |
|  | Read model data |
| Guest receive model data |  |
| Successfully read data |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| Guest input wrong model data format |  |
|  | Receive model data |
|  | Verify model data |
|  | Find exception |
| Guest receive exception |  |
| Failed to store data |  |
| Guest input model read request |  |
|  | Verify request |
|  | Model does not exist |
|  | Find exception |
| Guest receive exception |  |
| Failed to read data |  |

### Case: Motion data of sensors

- Version: 1
- Created: Apr 1
- Authors: Wenxuan ZHU
- Source: Motion data of sensors
- Actors: Store, modify and read
- Goal: Store, modify and read motion data
- Summary: Store the motion data in the database so that it can be read and used 
- Trigger: Data needs to be Stored
- Frequency: Every time train or prediction 
- Precondition: The data is used to train the model or needs to be predicted
- Postconditions: Data is in correct format 

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5428.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Guest input motion data |  |
|  | Receive motion data |
|  | Verify motion data |
|  | Store motion data  |
| Guest receive motion data |  |
| Successfully store data |  |
| Guest input data read request |  |
|  | Verify request |
|  | Read motion data |
| Guest receive motion data |  |
| Successfully read data |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| Guest input wrong motion data format |  |
|  | Receive motion data |
|  | Verify motion data |
|  | Find exception |
| Guest receive exception |  |
| Failed to store data |  |
| Guest input motion read request |  |
|  | Verify request |
|  | data does not exist |
|  | Find exception |
| Guest receive exception |  |
| Failed to read data |  |

### Case: Store the prediction result

- Version: 1
- Created: Mar 30
- Authors: Wenxuan ZHU
- Source: Store the prediction result
- Actors: Store and read
- Goal: Store and read the prediction result
- Summary: Store the prediction results in the database for easy reading 
- Trigger: The model predicts the motion data
- Frequency: Every time predict
- Precondition: Model and motion data are ready
- Postconditions: The result of prediction are reasonable

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba542a.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Guest input prediction result |  |
|  | Receive prediction result |
|  | Verify prediction result |
|  | store prediction result |
| Guest receive prediction result |  |
| Successfully store prediction result |  |
| Guest input result read request |  |
|  | Verify request |
|  | Read prediction result |
| Guest receive prediction result |  |
| Successfully read result |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| Guest input wrong prediction result |  |
|  | Receive prediction result |
|  | Verify prediction result |
|  | Find exception |
| Guest receive exception |  |
| Failed to store prediction result |  |
| Guest input result read request |  |
|  | Verify request |
|  | prediction result does not exist |
|  | Find exception |
| Guest receive exception |  |
| Failed to read prediction result |  |

### Case: Algorithm Output prediction results

- Version: 1
- Created: Apr 2
- Authors: Cong HUA
- Source: Server
- Actors: Algorithm
- Goal: Algorithm Output prediction results
- Summary: After prediction,  Algorithm will output the prediction results
- Trigger: Algorithm output the results
- Frequency: To be determined 
- Precondition: When Algorithm has finished making predictions 
- Postconditions: When Algorithm has finished making predictions 

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba542b.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Algorithm input prediction results |  |
|  | Receive the prediction result |
|  | Return prediction to the  Interface |
|  | Return success |
| Algorithm receive prediction-shown-successfully confirmation |  |
|  |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

<!-- XXQ start !-->
<!-- Northstar !-->
### Case: Get the pretrained model

- Version: 1
- Created: 2022-4-2
- Authors: Changjiang Zhou
- Source: \
- Actors: Server
- Goal: Initialize the system for the general audience.
- Summary: Get the pretrained model of the chosen algorithm.
- Trigger: Server calls this module.
- Frequency: Once every time the server wants to initialize the system.
- Precondition: 
  1. Models of all algorithms have been pretrained offline.
  2. Server has transferred the selected algorithm.
  3. Default algorithm is is explicitly defined.
- Postconditions: The corresponding general model have been activated for further operation of fune-tune.

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba540d.png)


#### Basic Flow

| Actor | System |
| ----- | ------ |
|  |Parameters of all pretrained models are uploaded to the database. |
|Server sends messages to get the pretrained model of the selected algorithm.| System finds the corresponding parameters of the selected algorithm from the database. |
|  | System backups the parameters for further operation of fine-tune.|
|  |System reads the parameters.  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| Server select a model that database haven’t prepared.| Send back the exception to the server call. |
| Database send the exception for reaching the model parameter| Send back the exception to the server call.|
|Failed to create the model on the device for some reasons. | Send the device error to the server call. |

### Case: Fine-tune the model

- Version: 1
- Created: 2022-4-2
- Authors: Changjiang Zhou
- Source: \
- Actors: Server
- Goal: Change the active model by real-time data.
- Summary: Adjust the parameters of the active model.
- Trigger: Server call this module.
- Frequency: Once every time a specific amount of real-time data is collected.
- Precondition: 
     1.	The system has been initialized.
     2.	A batch of labeled data derived from the sensors have been obtained and transfered.
     3.	The amount of data required for one iteration is pre-defined and collected.
- Postconditions: The parameter of the active model is fine-tuned by incrementally training the obtained real-time data.
![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5414.png)


#### Basic Flow

| Actor | System |
| ----- | ------ |
| Server sends a specific amount of real-time data with labels.  | System receives the input data. |
|  |System cleans invalid or noisy data.|
|  | System format the input data. |
|  | System incrementally trains the model using the formated data. |
|  | System saves new parameters to the database. |


#### Alternative Flow

| Actor | System |
| ----- | ------ |
|Database failed to send training data for some reason for a long run.| Raise the error back to the server |
| Training data is not well formatted for further process. |Raise the error back to the server  |


### Case: Predict the result

- Version: 1
- Created: 2022-4-2
- Authors: Changjiang Zhou
- Source: Predict the next motion pattern.
- Actors: Server
- Goal: Acquire the user’s next motion pattern.
- Summary: Server call this module.
- Trigger: Server call this module.
- Frequency: Follow the pre-defined frequency of prediction.
- Precondition:
     1.	The real-time data of a recent time window has been stored in the database.
     2.	The frequency of prediction is pre-defined.

- Postconditions: Server get the predicted motion pattern.


#### Basic Flow

| Actor | System |
| ----- | ------ |
|Server transfers real-time data. to predict the next motion pattern.	|System receive the input data.|
||	System formats the input data.|
||	System predicts the next motion pattern by the active model.|
||	System return the result to Server.|




#### Alternative Flow

| Actor | System |
| ----- | ------ |
|The server developer calls this algorithm program by sending real-time sensor data.	|Algorithm program receive the input.|
|The server stops the study of the algorithm.	||
||	The algorithm program ends and delete data.|


### Case: Select the algorithm

- Version: 1
- Created: 2022-4-2
- Authors: Changjiang Zhou
- Source: \
- Actors: Server
- Goal: Change the algorithm to achieve different performance(precision, recall, effectiveness or efficiency).
- Summary: Change the algorithm being used.
- Trigger: Server call this module.
- Frequency: Once every time the user wants to select a new specific algorithm.
- Precondition: 
     1.	All algorithms are implemented.
     2.	The target algorithm is transfered.
- Postconditions: The target algorithm is chosen.

#### Basic Flow

| Actor | System |
| ----- | ------ |
|Server calls the algorithm module by transfering the target algorithm the user wants to select. |	System receives the target algorithm the user wants to select.|
||	System reads the latest paramter if the algorithm has been chosen and adjusted before.|


#### Alternative Flow

| Actor | System |
| ----- | ------ |
|Server select a model that database haven’t prepared.	|Send back the exception to the server call.|
|Database send the exception for reaching the model parameter|	Send back the exception to the server call.|
|Failed to obtain the fine-tined model parameter.|	System reads the initialized general parameter if the algorithm is chosen for the first time.|

<!-- Furia !-->
### Case: Application wants the prediction of motions

- Version: 1
- Created: 4-2-22
- Authors: Siqi Guo
- Source: Algorithm
- Actors: Server
- Goal: Predict the personal intention according to the new-coming series of motions 
- Summary: receive motion data stream, predict the next motion periodically, and return the prediction result to the server
- Trigger: A real-time timer
- Frequency: The minimum affordable interval between two continuous queries depends on the performance of the actual neural network.
- Precondition: 
     - The prediction model is ready
     - The data stream has been established
- Postconditions: The result is in a reasonable range

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5423.png)


#### Basic Flow

| Actor | System |
| ----- | ------ |
|Server input motion data stream||	
||	Receive motion data stream|
||	Data clean|
||	Analysis data|
||	Get the prediction result|
||	Return the result|
|Server receive prediction result	||


### Case: Application wants an adjustable network structure

- Version: 1
- Created: 4-2-22
- Authors: Siqi Guo
- Source: Algorithm
- Actors: Server
- Goal: Adjust the model provided the new-coming series of motions in comparison of the prediction results and actual movement
- Summary: Different users have different traits of motion and a universal model can’t do well for all type of users.  Therefore, the network should be adjusted in the prediction process, and the save the adjusted model in database.
- Trigger: A real-time timer
- Frequency: One adjustment per 10 seconds
- Precondition: The prediction model is ready
- Postconditions: /

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5425.png)


#### Basic Flow

| Actor | System |
| ----- | ------ |
|Database update the data	||
||	Ask database to visit new data|
||	Visit new data|
||	Find the new part|
||	Update the prediction model|
||	Send new model to Server|
|Server receive new model	||


<!--- XYF start !--->

### Case: User Wants to Register

- Version: 1.0
- Created: Mar 31
- Authors: Jiazheng Pan, Haotian Tang, Weibin Cheng
- Source: /
- Actors: End user
- Goal: The user would like to register an account to access the software.
- Summary: The user input all the necessary information as well as captcha and then get a new account.
- Trigger: The user wants to get an account so he/she can use the software.
- Frequency: Usually just once, before starting to use the software.
- Precondition: The Internet is available and the registration page is displayed.
- Postconditions: Automatically log in with the lastly registered account.

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5407.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Click the registration button |  |
| Input the necessary information including e-mail |  |
|  | Send the captcha to the e-mail |
| Input the captcha |  |
|  | Generate a new account |
| Receive a notification and enter the software |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| From basic flow 2 |  |
| Input illegal  registration information such as wrong e-mail address or too short password |  |
|  | Prompts the user,  gives the correct format and locks the ‘next step’ button |
|  | Prompts the users of wrong captcha |
| User corrects the information entered |  |
|  | Go to basic flow Step 3 |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| From basic flow step 4 |  |
|  | Send the captcha to the e-mail |
| Input wrong captcha and click sign up button |  |
|  | Prompts the users of wrong captcha |
| User corrects the captcha |  |
|  | Go to basic flow step 5 |


### Case: User Wants to Login


- Version: 1.0
- Created: Mar 31
- Authors: Jiazheng Pan, Haotian Tang, Weibin Cheng
- Source: /
- Actors: End user
- Goal: The user would like to log in the account.
- Summary: The user input the username and password, and if it’s correct, then jump to the main page.
- Trigger: The user wants to enter the software and use it.
- Frequency: Every time before the user enter the software.
- Precondition: The user already has an account and the login page is displayed.
- Postconditions: Jump to the main page of the software.

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Input the username and password |  |
|  | Determine whether they match |
|  | If match, jump to the main page |
|  | If not, prompt password error |
| Enter the main page |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| From basic flow step 1 |  |
| Inputs wrong user name or password |  |
|  | Prompts the user of wrong or unmatched user name and password |
| Corrects the user name and/or password |  |
|  | Go to basic flow step 5 |

### Case: User Wants to View The Status of The System

- Version: 1.0
- Created: Mar 31
- Authors: Jiazheng Pan, Haotian Tang, Weibin Cheng
- Source: /
- Actors: End user
- Goal: The user wants to view the current status of the system, such as connection status, work status, etc.
- Summary: The user selects “the status of the model” page and can see the related status in the page. So the user can decide what to do next.
- Trigger: The user wants to know what to do according to the system status.
- Frequency: Uncertain, according to the user.
- Precondition: The user has logged in and the system is running normally.
- Postconditions: The current status of the system is displayed in the page.

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Select "the status of the model" page |  |
|  | Show the current system status |
| See the system status |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| From basic flow step 1 |  |
|  | Failed to connect to the server |
|  | Prompt the user of network failure |
| Go to basic flow step 1 |  |


### Case: User Wants to Add a New Device to The System

- Version: 1.0
- Created: Mar 31
- Authors: Jiazheng Pan, Haotian Tang, Weibin Cheng
- Source: /
- Actors: End user
- Goal: The user wants to add a new sensor to the system.
- Summary: The user select the “add devices” option and chooses the certain device in the detection list. Then the device is connected to the system.
- Trigger: The user wants to use a device to record motions.
- Frequency: Every time a new device is used.
- Precondition: The user has logged in. The motion device is available and can link the Internet.
- Postconditions: The new added device can be seen in the device list.

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Get the new device and activate it |  |
| Select the “add device” option |  |
|  | Scan all devices within range |
|  | Show the detected devices |
| Choose the corresponding device |  |
|  | Add the chosen device to the system |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
|  | From basic flow step 4 |
| Cannot find the expected device |  |
| Check the availability of the device |  |
| Go to basic flow step 1 |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
|  | From basic flow step 6 |
|  | Fails to add the chosen device |
|  | Prompts the user of failure and its reason |
| Check the availability of the device |  |
| Go to basic flow step 1 |  |


### Case: User wants to start record motions

- Version: 1.0
- Created: Mar 31
- Authors: Jiazheng Pan, Haotian Tang, Weibin Cheng
- Source: /
- Actors: End user
- Goal: The user wants to use the device to record motions.
- Summary: The user click the “start/stop” button to start or stop recording motions and does some movements next.
- Trigger: The user wants to collect new data.
- Frequency: Every time the user wants to collect some data.
- Precondition: The user has logged in. The device is intact and is connected to the system.
- Postconditions: The motions are recorded and temporally stored.

#### Basic Flow

|  Actor	| System |
| ----- | ------ |
| Click the “start” button |  |
| Do some movements	|  |
|  | Start to record with the device |
| Pause/continue the recording |  |
| Click the “stop” button |  |
|  | Finish recording and store the data temporally |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| From basic flow step 2 |  |
|  | Fails to track user’s movement due to broken connection, e.t.c. |
|  | Prompts the user of failure and its reason |
| Go to basic flow step 1 |  |


### Case: User wants to upload/discard the data

- Version: 1.0
- Created: Mar 31
- Authors: Jiazheng Pan, Haotian Tang, Weibin Cheng
- Source: /
- Actors: End user
- Goal: The user wants to upload/ discard the collected data.
- Summary: The user chooses the “upload” or “discard” button to decide whether 
- Trigger: The user wants to deal with the collect data in order for the next recording
- Frequency: Every time the recording is successfully completed.
- Precondition: The user has logged in. The recording is stopped and the motions are successfully collected.
- Postconditions: The collected data is uploaded to the database or discarded.

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Click “upload” or “discard” button|  |
|  | Upload the data to the database or discard it |
|  | Show processing results |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
|  | From basic flow step 2 |
|  | Fails to upload the data to the server due to network congestion or broken connection |
|  | Prompts the user of failure and its reason |
| Go to basic flow 1 |  |


### Case: User wants to individualize the model

- Version: 1.0
- Created: Mar 31
- Authors: Jiazheng Pan, Haotian Tang, Weibin Cheng
- Source: /
- Actors: End user
- Goal: The user wants to individualize the model with the collected data to adaptively make predictions.
- Summary: The user selects the “individualize” option and let the system train the model with the new data. Then use the new model to predict.
- Trigger: The user wants to finetune the existing model.
- Frequency: Every time the user wants to finetune the model.
- Precondition: The user has logged in. Some new data is collected and uploaded.
- Postconditions: The existing model is trained and the finetuned model is ready for prediction.

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5427.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Select a certain basic model |  |
| Select “individualize” option |  |
|  | Train the chosen model with the new data |
|  | Display the loss function and related index |
| Synchronize the newly trained model when finishing |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| From basic flow step 5 |  |
|  | Fails to synchronize the newly trained model due to certain reason such as network disconnection |
|  | Prompts the user of failure and its reason |
| Go to basic flow step 5 |  |

### Case: User wants to reset the model

- Version: 1.0
- Created: Mar 31
- Authors: Jiazheng Pan, Haotian Tang, Weibin Cheng
- Source: /
- Actors: End user
- Goal: The user wants to reset the finetuned model to the initial state.
- Summary: The user selects the “reset” option and clear the newly finetuned model, resetting it to the initial state.
- Trigger: The user doesn’t want to use the new model.
- Frequency: Uncertain, according to the user.
- Precondition: The user has logged in. There is a model that has been trained with the new data.
- Postconditions: The newly trained model is restored.

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Select the “reset” option |  |
|  | Download the original model from server |
|  | Discard the old model |
|  | Reset the model to the initial state |
| Receive successful tips |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
|  | From basic flow step 2 |
|  | Downloads fails due to insufficient memory, network anomaly or other unknown reason |
|  | Prompts the user of failure and its reason |
| Go to basic flow step 1 |  |

### Case: Register a New Account

- Version: 1
- Created: Mar 30
- Authors: Haozhen ZHANG, Zhikang TAN
- Source: /
- Actors: End User
- Goal: Register a New Account
- Summary: Users get an account by submitting personal information
- Trigger: The end user clicks on the "Register" option in the login interface
- Frequency: Usually only once per user
- Precondition: The application is open and running
- Postconditions: User gets a new account and can use it to log in to the application

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba542c.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| From the login interface, the user selects the "Register" option and enter register interface. |  |
| User input personal information (e.g. email, password, etc.) |  |
|  | Receive and verify user’s personal information  |
|  | Create a new account and return the account successfully |
| Receive the new created account and make a confirmation |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| 1. The user has not input all the personal information or some information is not valid |  |
| 2. Unable to connect to the server due to network etc |  |
|  | 1.	Warn the user to fill in all personal information correctly |
|  | 2.	Prompts for user register failure |

### Case: Log in to the Application

- Version: 1
- Created: Mar 30
- Authors: Haozhen ZHANG, Zhikang TAN
- Source: /
- Actors: End User
- Goal: The end user can log in to the application so that they can add equipment and collect data
- Summary: The user enters the account and password and starts to use software after application verifies
- Trigger: The end user inputs account and password and clicks on the "Login" option in the login interface
- Frequency: Once before use software
- Precondition: The application is open and running
- Postconditions: The application is running, waiting for its next instruction from the end user

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba542d.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| The end user inputs account and password and clicks on the "Login" option in the login interface |  |
|  | The end user inputs account and password and clicks on the "Login" option in the login interface |
| Log in successfully |  |
#### Alternative Flow

| Actor | System |
| ----- | ------ |
| 1.	The account or password user input is incorrect or invalid |  |
| 2.	Unable to connect to the server due to network etc |  |
|  | 1.	Warn the user to input correct account and password |
|  | 2.	Prompts for user login failure |

### Case: View User Information

- Version: 1
- Created: Mar 30
- Authors: Haozhen ZHANG, Zhikang TAN
- Source: /
- Actors: End User
- Goal: The end user can view and change the user information
- Summary: Users view and change their registration information on the application
- Trigger: The user enters the “User Information” interface after logging in
- Frequency: /
- Precondition: The application is open and running. User has logged in
- Postconditions: User information should be permanently changed and the next time the end user views user information or logs in, the changed information should be displayed

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba542f.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| User enters the “User Information” interface after logging in |  |
| View user information and change some of the information |  |
|  | Receive and verify changed information |
|  | Change information from the database and return confirmation message |
| Receive message and make a confirmation |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| The information after user changes is invalid or incorrectly formatted. |  |
|  | The information after user changes is invalid or incorrectly formatted. |
|  | Warn the user to input correct information |

### Case: Add Equipment

- Version: 1
- Created: Mar 30
- Authors: Haozhen ZHANG, Zhikang TAN
- Source: /
- Actors: End User
- Goal: The user can establish a connection with the equipment so that the data can be collected
- Summary: The user selects the equipment that can be connected, and once connected application creates a component to display the newly added equipment
- Trigger: The user selects the "add" option in “equipment” interface
- Frequency: Once when adding equipment
- Precondition: The application is open and running. User has logged in
- Postconditions: The application prompts the user that the equipment has been added successfully. The status of new added equipment is displayed in the component into the GUI. The user can select the component to manipulate it further

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5430.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| The user selects the "add" option in “equipment” interface |  |
|  | Return the equipment to which connections can be established |
| Select and confirm the equipment |  |
|  | Establish the connection to the selected equipment |
|  | Create components in the GUI to display the newly added equipment and return confirmation message |
| Receive message and make a confirmation |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| 1.	The waiting added equipment is closed, corrupted, etc |  |
| 2.	Failed to add due to network etc |  |
|  | 1.	Warn the user that the equipment has failed |
|  | 2.	Prompts the user for the add failure |

### Case: Check the Status of the Equipment

- Version: 1
- Created: Mar 30
- Authors: Haozhen ZHANG, Zhikang TAN
- Source: /
- Actors: End User
- Goal: The end user can check the connection status of all equipment to ensure that data can be collected properly
- Summary: Users can view the status of each connected equipment
- Trigger: The user enters “equipment” interface after logging in
- Frequency: /
- Precondition: The user enters “equipment” interface after logging in
- Postconditions: The status of all equipment should be accurately displayed in real time on the components of the main working window

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5431.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| The user enters “equipment” interface after logging in |  |
|  | Display the status of all equipment |
| View connection status of all added equipment |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| The added equipment is closed, corrupted, etc |  |
|  | Update the corresponding equipment status or warn user equipment has been disabled |

### Case: View Equipment Details

- Version: 1.0
- Created: Mar 30
- Authors: Zhang Haozhen、Tan Zhikang
- Source: /
- Actors: End User
- Goal: The user can view details of all equipment and disconnect from the equipment
- Summary: /
- Trigger: The end user selects one of the components which are used to display the status of equipment
- Frequency: /
- Precondition: The application is open and running. User has logged in. There is equipment being added.
- Postconditions: The status of all equipment should be accurately displayed in real time on the components of the main working window

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba542e.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| The end user selects one of the components which are used to display the status of equipment |  |
|  | Create a new window to display the detail of the equipment |
| View detail of the equipment. Confirm and close the new window |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| User wants to disconnect from the equipment and confirm the "disconnect" option |  |
| The added equipment is closed, corrupted, etc |  |
|  | Disconnect from the equipment and prompt |
|  | Update the corresponding equipment status or warn user equipment has been disabled |
|  | The new window is closed. The component of the disconnected equipment disappears |

### Case: View Usage Guide

- Version: 1.0
- Created: Mar 30
- Authors: Zhang Haozhen、Tan Zhikang
- Source: /
- Actors: End User
- Goal: The user is able to access information about the function of each function key.
- Summary: When the user's mouse hovers over a function key, the user is able to access information about its function
- Trigger: The user's mouse hovers over a function key
- Frequency: /
- Precondition: The application is open and running. User has logged in
- Postconditions: User should be able to obtain detailed function instructions when user’s mouse hovers over a function key

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5432.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| The user hovers his mouse over a function key |  |
|  | Show function information of the function key |


### Case: Start to Collect Data

- Version: 1.0
- Created: Mar 30
- Authors: Zhang Haozhen、Tan Zhikang
- Source: /
- Actors: End User
- Goal: The user would like to determine the start and end of data collection and the application stores the collected data temporarily
- Summary: The user clicks on the "start" option to start collecting data, the "stop" option to stop collecting, or the "retry" option to re-collect. During this time, the application temporarily stores the collected data
- Trigger: User enters the “data” interface and selects the “start” option
- Frequency: Once when user wants to collect data.
- Precondition: The application is open and running. All equipment has been added and is working properly
- Postconditions: The user can decide whether to upload or discard the collected data and then application returns to the state before data collection

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5433.png)


#### Basic Flow

| Actor | System |
| ----- | ------ |
| User enters the “data” interface and selects the “start” option |  |
|  | Start collecting data and store the collected data temporarily |
| Select the “stop” option |  |
|  | Stop collecting data |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
| Collection failure due to network etc. |  |
| User wants to restart data collection and selects the “retry” option | Prompt user to check network and other issues before recollection |
|  | Stop collecting data and remind user whether to upload data |
| Decide to upload or discard data |  |
|  | Upload or discard data according to user’s selection |


### Case: Upload the Collected Data

- Version: 1.0
- Created: Mar 30
- Authors: Zhang Haozhen、Tan Zhikang
- Source: /
- Actors: End User
- Goal: The user would like to upload the collected data to the database
- Summary: After the data has been collected, the user clicks on the “upload” option to upload the data to the database
- Trigger: User select “upload” option after data has been successfully collected
- Frequency: Once or zero times after collecting data
- Precondition: The application is open and running. l equipment has been added and is working properly. Data has been successfully collected
- Postconditions: Upload the collected data. Application returns to the state before data collection waiting for its next instruction from the end user

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5434.png)


#### Basic Flow

| Actor | System |
| ----- | ------ |
| User select “upload” option after data has been successfully collected |  |
|  | Upload the collected data |
|  | Prompt user after completing the upload |
| Receive message and make a confirmation |  |

#### Alternative Flow

| Actor | System |
| ----- | ------ |
|  | Fails to upload the collected data due to network etc |
|  | Prompt user for upload failure and Return to the previous state |
| Receive message and make a confirmation |  |

### Case: Discard the Collected Data

- Version: 1.0
- Created: Mar 30
- Authors: Zhang Haozhe, Tan Zhikang
- Source: /
- Actors: End User
- Goal: The user would like to clear the collected data from the application
- Summary: After the data has been collected, the user clicks on the "discard" option to discard the temporarily stored data
- Trigger: User select “discard” option after data has been successfully collected
- Frequency: Once or zero times after collecting data
- Precondition: The application is open and running. l equipment has been added and is working properly. Data has been successfully collected
- Postconditions: Application returns to the state before data collection waiting for its next instruction from the end user. The application no longer has any trace of data that has just been discarded

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5435.png)


#### Basic Flow

| Actor | System |
| ----- | ------ |
| User select “discard” option after data has been successfully collected |  |
|  | Discard the collected data |
|  | Prompt user after completing the discard |
| Receive message and make a confirmation |  |


<!--- BY start !--->

<!-- Happy Family (DB) ~ Interaction -->

### Case: Interaction wants to store user personal information in the database

- Version: 1
- Created: Mar. 30
- Authors: Yiruo Cheng
- Source: Server
- Actors: Interaction
- Goal: Store the registration information of user
- Summary: Add User ID, Add password, Add related e-mail
- Trigger: The end user selects the "Register" option
- Frequency: 
- Precondition: The application is open and running
- Postconditions: The user personal information is stored in the database

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5402.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| From the Interaction menu, the end user selects the "Register" option | |
| | User ID, password and related e-mail are transported to the database by the server |
| | Database store the user ID, password and related e-mail |
| The end user registered successfully | |


#### Alternative Flow

| Actor | System |
| ----- | ------ |
| From the Interaction menu, the end user selects the "Register" option | |
| | User ID, password and related e-mail are transported to the database by the server |
| | This e-mail has been registered |
| The end user registered unsuccessfully | |


### Case: Interaction wants to use user personal information to login in the database

- Version: 1
- Created: Mar. 30
- Authors: Yiruo Cheng
- Source: Server
- Actors: Interaction
- Goal: Check the user personal information and verify
- Summary: Add User ID, Add password, Add related e-mail
- Trigger: The end user selects the "Login" option
- Frequency: 
- Precondition: The application is open and running and the user personal information has been stored in the database
- Postconditions: Interaction dispalys a feedback for successful login

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Interaction wants to use user personal information to login | |
| | User ID, password and related e-mail are transported to the database by the server |
| | Find the User ID, and check  the corresponding password. |
| | Find the User ID and the password is correct. |
| Interaction dispalys a feedback for successful login | |


#### Alternative Flow

| Actor | System |
| ----- | ------ |
| Interaction wants to use user personal information to login | |
| | User ID, password and related e-mail are transported to the database by the server |
| | Find the User ID, and check  the corresponding password |
| | Find the User ID and the password is wrong |
| Interaction dispalys a feedback for unsuccessful login | |

### Case: Interaction wants to change user personal information in the database

- Version: 1
- Created: Mar. 30
- Authors: Yiruo Cheng
- Source: Server
- Actors: Interaction
- Goal: Change the user personal information 
- Summary: Change the password and the related e-mail
- Trigger: The end user selects the "Change" option
- Frequency: 
- Precondition: The application is open and running, and the user personal information has been stored in the database
- Postconditions: Interaction dispalys a feedback for successful change and the changed user information is stored in the database

![](https://doc.ciel.pro/uploads/330b3aef93b0cd2a1c8ba5406.png)

#### Basic Flow

| Actor | System |
| ----- | ------ |
| The end user selects the "Change" option | |
| The end user input the original password and the new word twice | |
| The end user clicks the "yes" button | |
| The interaction check whether the two new password is the same | |
| | User ID, original password and  new password are transported to the database by the server |
| | Find the User ID, and check  wheter the original password is correct |
| | Change the password in the database |
| Interaction dispalys a feedback for successful change | |


#### Alternative Flow

| Actor | System |
| ----- | ------ |
| The end user selects the "Change" option | |
| The end user input the original password and the new word twice | |
| The end user clicks the "yes" button | |
| The interaction check whether the two new password is the same | |
| | User ID, original password and  new password are transported to the database by the server |
| | Find the User ID, and check  wheter the original password is wrong |
| Interaction dispalys a feedback for unsuccessful change | |

<!-- Happy Family (DB) ~ Algorithm -->

### Case: Algorithm Wants to Save the Algorithm model in Binary form

- Version: 1
- Created: Mar. 30
- Authors: Xiangping Deng
- Source: Server
- Actors: Algorithm
- Goal: The algorithm wants to store their algorithm model in database in order to use it to predict the action of users
- Summary: 
- Trigger: 
- Frequency: 
- Precondition: Algorithm has trained their model
- Postconditions: The algorithm model has been stored in the database

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Algorithm send the model in binary to the Server | |
| | Server sends the model to Database |
| | Database stores it |


#### Alternative Flow

| Actor | System |
| ----- | ------ |
| Algorithm send the model in binary to the Server | |
| | Server sends the model to Database |
| | Incomplete or incorrect information in the model file |
| | The database stores and specially labels it |


### Case: Algorithm Wants to Save Relevant Datasets

- Version: 1
- Created: Mar. 30
- Authors: Xiangping Deng
- Source: Server
- Actors: Algorithm
- Goal: The algorithm wants to store the datasets and results of the train in the database
- Summary: 
- Trigger: 
- Frequency: 
- Precondition: Algorithm has trained their model
- Postconditions: The database has stored the datasets and the results

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Algorithm send the model in binary to the Server | |
| | Database stores the datasets and results in database |
| | Algorithm gets the relevant data from the database to train the model |
| | The model has runed |
| | Algorithm sends the results to Server |
| | Server sends the results to database |
| | Database stores it |


#### Alternative Flow

| Actor | System |
| ----- | ------ |
| Algorithm send the model in binary to the Server | |
| | Database stores the datasets and results in database |
| | Algorithm gets the relevant data from the database to train the model |
| | The model has runed |
| | Algorithm sends the results to Server |
| | Server sends the results to database |
| | Incomplete or incorrect information in the results |
| | Database stores and specially labels it |


### Case: Algorithm Wants to Save the Results of trained sensor data

- Version: 1
- Created: Mar. 30
- Authors: Xiangping Deng
- Source: Server
- Actors: Algorithm
- Goal: The algorithm wants to store the results of the sensor data from Sever in the database
- Summary: 
- Trigger: 
- Frequency: 
- Precondition: Database has stored the sensor data, and Algorithm has got the sensor data, trained their model, and run the sensor data in their model
- Postconditions: The database has stored the results

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Algorithm | |
| | Algorithm sends the results to the database by the server |
| | Database stores it |


#### Alternative Flow

| Actor | System |
| ----- | ------ |
| Algorithm | |
| | Algorithm sends the results to the database by the server |
| | Incomplete or incorrect information in the results |
| | Database stores and specially labels it |


### Case: Algorithm Wants to Save the performance metrics of the Algorithm model

- Version: 1
- Created: Mar. 30
- Authors: Xiangping Deng
- Source: Server
- Actors: Algorithm
- Goal: The algorithm wants to store the performance metrics of the Algorithm model in database
- Summary: 
- Trigger: 
- Frequency: 
- Precondition: Algorithm has trained their model and run the sensor data in their model
- Postconditions: The database has stored the performance metrics of the Algorithm model

#### Basic Flow

| Actor | System |
| ----- | ------ |
| Algorithm | |
| | Algorithm has run the model |
| | Database stores it |
| | Algorithm sends the performance metrics to Server |
| | Server sends the performance metrics to database |
| | Database stores it |


#### Alternative Flow

| Actor | System |
| ----- | ------ |
| Algorithm | |
| | Algorithm has run the model |
| | Database stores it |
| | Algorithm sends the performance metrics to Server |
| | Server sends the performance metrics to database |
| | Incomplete or incorrect information in the results |
| | Database stores and specially labels it |

### Case: Calling API for register and login

- Version: 1
- Created: 2022.4.1
- Authors: Qian Yuhang
- Source: Database
- Actors: Server
- Goal: Saving user data and querying information from MySQL
- Summary: Create a instance of class “DatabaseManager” with all database access functions.
- Trigger: When use “DatabaseManager”
- Frequency: /
- Precondition: MySQL is running and is correctly connected.
- Postconditions: The information in MySQL should be correctly stored and must fit the limitation of the table structure.


#### Basic Flow

| Actor | System |
| ----- | ------ |
|Call API for register and login	||
||	Function receive some parameters|
||	Access MySQL for information|
||	Check the result and return it|
|API request finished	||


#### Alternative Flow

| Actor | System |
| ----- | ------ |
|Calling API with invalid parameters||	
||	Function receive some parameters|
||	Throw an error “Wrong Parameters”|
|API request unsuccessfully	||


### Case: Calling API for changing information

- Version: 1
- Created: 2022.4.1
- Authors: Qian Yuhang
- Source: Database
- Actors: Server
- Goal: Change user data in MySQL
- Summary: Create a instance of class “DatabaseManager” with all database access functions.
- Trigger: When use “DatabaseManager”
- Frequency: /
- Precondition: MySQL is running and is correctly connected.
- Postconditions: The information in MySQL should be correctly stored and must fit the limitation of the table structure.


#### Basic Flow

| Actor | System |
| ----- | ------ |
|Call API for changing information	||
||	Function receive some parameters|
||	Access MySQL for information|
||	Check the result and return it|
|API request finished	||

#### Alternative Flow

| Actor | System |
| ----- | ------ |
|Calling API with invalid parameters	||
||	Function receive some parameters|
||	Throw an error “Wrong Parameters”|
|API request unsuccessfully	||

### Case: Upload and download sensor data.

- Version: 1
- Created: 2022.4.1
- Authors: Qian Yuhang
- Source: Database
- Actors: Server
- Goal: Change user data in MySQL
- Summary: Create a instance of class “DatabaseManager” with all database access functions.
- Trigger: When use “DatabaseManager”
- Frequency: /
- Precondition: MySQL is running and is correctly connected.
- Postconditions: The information in MySQL should be correctly stored and must fit the limitation of the table structure.


#### Basic Flow

| Actor | System |
| ----- | ------ |
|Call API for Upload and download sensor data.	||
||	Function receive some parameters|
||	Access MySQL for information|
||	Check the result and return it|
|API request finished	||


#### Alternative Flow

| Actor | System |
| ----- | ------ |
|Calling API with invalid parameters	||
||	Function receive some parameters|
||	Throw an error “Wrong Parameters”|
|API request unsuccessfully	||


### Case: Upload and download the trained model

- Version: 1
- Created: 2022.4.1
- Authors: Qian Yuhang
- Source: Database
- Actors: Algorithm and Server
- Goal: Change user data in MySQL
- Summary: Create a instance of class “DatabaseManager” with all database access functions.
- Trigger: When use “DatabaseManager”
- Frequency: /
- Precondition: MySQL is running and is correctly connected.
- Postconditions: The information in MySQL should be correctly stored and must fit the limitation of the table structure.


#### Basic Flow

| Actor | System |
| ----- | ------ |
|Call API for upload and download network model.	||
||	Function receive some parameters|
||	Access MySQL for information|
||	Check the result and return it|
|API request finished	||


#### Alternative Flow

| Actor | System |
| ----- | ------ |
|Calling API with invalid parameters	||
||	Function receive some parameters|
||	Throw an error “Wrong Parameters”|


