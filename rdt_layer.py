from segment import Segment
import time

# #################################################################################################################### #
# RDTLayer                                                                                                             #
#                                                                                                                      #
# Description:                                                                                                         #
# The reliable data transfer (RDT) layer is used as a communication layer to resolve issues over an unreliable         #
# channel.                                                                                                             #
#                                                                                                                      #
#                                                                                                                      #
# Notes:                                                                                                               #
# This file is meant to be changed.                                                                                    #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #


class RDTLayer(object):
    # ################################################################################################################ #
    # Class Scope Variables                                                                                            #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    DATA_LENGTH = 4 # in characters                     # The length of the string data that will be sent per packet...
    FLOW_CONTROL_WIN_SIZE = 15 # in characters          # Receive window size for flow-control
    sendChannel = None
    receiveChannel = None
    dataToSend = ''
    currentIteration = 0                                # Use this for segment 'timeouts'
    # Add items as needed
<<<<<<< HEAD
    TIMEOUT = 0.5                                       # Timeout
=======
    TIMEOUT = 0.5
    MAX_SEGMENTS = FLOW_CONTROL_WIN_SIZE // DATA_LENGTH  # How many full segments can we send within one window.
>>>>>>> d727ce3a7ccfc4fbbf93fe3470103b02ea3a74f8

    # ################################################################################################################ #
    # __init__()                                                                                                       #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def __init__(self):
        self.dataToSend = ''
        self.dataReceived = ''
        self.lastSegmentSent = None
        self.lastSegmentReceived = None
        self.sendChannel = None
        self.receiveChannel = None
<<<<<<< HEAD
        self.expectedSeqNum = 0                             # Sequence number the receiver is expecting
        self.nextSeqNum = 0                                 # Sequence number for sender
        self.lastAckReceived = -1                           #
        self.segmentTimeouts = 0                            # To count timeouts
        self.timeLastSegmentSent = time.time()              # RTT
=======
        self.expectedSeqNum = 0                          # Sequence number the receiver is expecting
        self.nextSeqNum = 0                              # Sequence number for sender
        self.lastAckReceived = -1
        self.segmentTimeouts = 0
        self.timeLastSegmentSent = time.time()
>>>>>>> d727ce3a7ccfc4fbbf93fe3470103b02ea3a74f8

    # ################################################################################################################ #
    # setSendChannel()                                                                                                 #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the unreliable sending lower-layer channel                                                 #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setSendChannel(self, channel):
        self.sendChannel = channel

    # ################################################################################################################ #
    # setReceiveChannel()                                                                                              #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the unreliable receiving lower-layer channel                                               #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setReceiveChannel(self, channel):
        self.receiveChannel = channel

    # ################################################################################################################ #
    # setDataToSend()                                                                                                  #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the string data to send                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setDataToSend(self,data):
        self.dataToSend = data

    # ################################################################################################################ #
    # getDataReceived()                                                                                                #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to get the currently received and buffered string data, in order                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def getDataReceived(self):
<<<<<<< HEAD
        return self.dataReceived

=======
        # ############################################################################################################ #
        # Identify the data that has been received...
        return self.dataReceived


        # ############################################################################################################ #

>>>>>>> d727ce3a7ccfc4fbbf93fe3470103b02ea3a74f8
    # ################################################################################################################ #
    # processData()                                                                                                    #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # "timeslice". Called by main once per iteration                                                                   #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def processData(self):
        self.currentIteration += 1
        self.processSend()
        self.processReceiveAndSendRespond()

    # ################################################################################################################ #
    # processSend()                                                                                                    #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Manages Segment sending tasks                                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def processSend(self):

        # ############################################################################################################ #
        # You should pipeline segments to fit the flow-control window
        # The flow-control window is the constant RDTLayer.FLOW_CONTROL_WIN_SIZE
        # The maximum data that you can send in a segment is RDTLayer.DATA_LENGTH
        # These constants are given in # characters

        # Somewhere in here you will be creating data segments to send.
        # The data is just part of the entire string that you are trying to send.
        # The seqnum is the sequence number for the segment (in character number, not bytes)
        # ############################################################################################################ #

<<<<<<< HEAD
        #--------------------------------------------------------------------------------------------------------------
        # Citation:
        #       I modeled the implementation of Go-Back-N from this YouTube video that was mentioned in the
        #       comment section on Ed Discussion. The source to the YouTube video is:
        #       https://www.youtube.com/watch?v=NMbMXCbYaX4&ab_channel=EpicNetworksLab
        #
        #       Starting at 5:03, he talks about how Go-Back-N works by showing a visual presentation of it. That is
        #       what I tried to implement here. It is buggy and needs to be completed.
        #
        #       The source to this Ed Discussion thread is: https://edstem.org/us/courses/41023/discussion/3322598
        # --------------------------------------------------------------------------------------------------------------
        # If there is still data to send, send only up to 4 characters per packet
=======
        # -------------------------------------------------------------------------------------------------------------
        #   Citations:
        #          I used the flowchart of the "Example Sequence Diagram" from Exploration: Programming Project Primer:
        #          Reliable Data Transmission to implement this function. For example, I wasn't sure how to send
        #          acknowledgment back to the client, so I used the logic from that exploration to decided whether
        #          to send the packet or retransmit.
        # -------------------------------------------------------------------------------------------------------------

>>>>>>> d727ce3a7ccfc4fbbf93fe3470103b02ea3a74f8
        if self.dataToSend:
            if not self.lastSegmentSent or (time.time() - self.timeLastSegmentSent) >= RDTLayer.TIMEOUT:
                segment = Segment()
                payload = self.dataToSend[:RDTLayer.FLOW_CONTROL_WIN_SIZE]
                segment.setData(self.nextSeqNum, payload)
                self.sendChannel.send(segment)
                self.lastSegmentSent = segment
                self.timeLastSegmentSent = time.time()

    # ################################################################################################################ #
    # processReceive()                                                                                                 #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Manages Segment receive tasks                                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def processReceiveAndSendRespond(self):

        # This call returns a list of incoming segments
        listIncomingSegments = self.receiveChannel.receive()

        # ############################################################################################################ #
        # What segments have been received?
        # How will you get them back in order?
        # This is where a majority of your logic will be implemented
        # ############################################################################################################ #

        # --------------------------------------------------------------------------------------------------------------
        # Citation:
        #       I modeled the implementation of Go-Back-N from this YouTube video that was mentioned in the
        #       comment section on Ed Discussion. The source to the YouTube video is:
        #       https://www.youtube.com/watch?v=NMbMXCbYaX4&ab_channel=EpicNetworksLab
        #
        #       Starting at 5:03, he talks about how Go-Back-N works by showing a visual presentation of it. That is
        #       what I tried to implement here. It is buggy and needs to be completed.
        #
        #       The source to this Ed Discussion thread is: https://edstem.org/us/courses/41023/discussion/3322598
        # --------------------------------------------------------------------------------------------------------------

        for segment in listIncomingSegments:
            # Check to see if the packet has been acknowledged
            if segment.acknum != -1:
                # If the acknum is in the window, then slide the window and update data to send.
                # This simple example assumes that the window size is represented as an integer.
                # The actual implementation should consider the exact window size and manage accordingly.
                while self.nextSeqNum <= segment.acknum and len(self.dataToSend) > 0:
                    self.dataToSend = self.dataToSend[RDTLayer.FLOW_CONTROL_WIN_SIZE:]
                    self.nextSeqNum += 1

            # It's a data segment
            else:
                # Expected segment received
                if segment.seqnum == self.expectedSeqNum and segment.checkChecksum():
                    self.dataReceived += segment.payload
                    ackSegment = Segment()
                    ackSegment.setAck(segment.seqnum)
                    self.sendChannel.send(ackSegment)
                    self.expectedSeqNum += 1

                # Out of sequence but we still send an ACK for the highest in-order segment received
                else:
                    ackSegment = Segment()
                    if self.lastSegmentReceived:
                        ackSegment.setAck(self.lastSegmentReceived.seqnum)
                        self.sendChannel.send(ackSegment)

            self.lastSegmentReceived = segment
    # -----------------------------------------------------------------------------------------------------------------
    # Citation:
    #       According to Ed Discussion, I had to create countSegmentTimeouts() function because when the server have
    #       received all the data, the output required me to show the number of segment timeouts. Originally, my program
    #       had the server receiving all the data and the program output the statistics for the packets that had been
    #       sent to the server from the client. However I had an error regarding not having a countSegmentTimeouts()
    #       function. Source: https://edstem.org/us/courses/41023/discussion/3308502
    #
    #       Also, when I added the function, I was still getting an error. I found this article that had great
    #       explanation how to combat errors when my rdt_main program from displaying the correct segment timeouts. The
    #       error then went away.
    #       Source: https://www.freecodecamp.org/news/python-property-decorator/#:~:text=The%20%40property%20is%20a%20built,of%20the%20use%20of%20%40property!
    # -----------------------------------------------------------------------------------------------------------------
    @property
    def countSegmentTimeouts(self):
        return self.segmentTimeouts
