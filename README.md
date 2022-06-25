 ## Flux: A data flow model

**Formally: pyConsole : Concept and Construction.**

**Check: [specification-LineBuffer.txt](specification-LineBuffer.txt)** .

`flux`: The primary motivation behind this library has been to differentate and parse different information sets arriving at a single port. To illustrate, let us consider a `Serival-device`  which **transmits** in different `channels`:

1. Data
2. Meta-data (information about the current device state)

And **receives**:

1. Commands from the parent device (assuming the parsing and interpretation of commands is not a concern of the parent device)

We assume that the different data streams are seperated by `\n` (endline) characters, and a unit is called `datum`. The `elements` of a datum can be internally seperated by `sep` characters, say spaces or tabs. Each datum starts with a `channel_id` that allows the `pyConsole` to identify the appropriate channel.

Apart from that, the datum starts with a `ch_count` which identifies the number of datum sent to that channel and hence, aids in the identification and bookeeping of lost datums.



Hence, a typical `datum` looks like (note: each element, including `meta-elements` are seperated by `sep`:

`| ch_count (optional) | sep | channel_id | sep | d1 | sep | d2 | sep | d3 | ... | sep | dn | \n` 



## Data Handling



### `class Parser`

Each datum is **split**, **cleaned**, **decoded** , and **time-tagged** by a parser.  It is a singleton object common to all channels and for serial devices - shares one `port`.



The parser has the followig functions:

```python
parser.register(port) #port may be replaced by any other stream
parser.open() # parser is open and listens to the stream
parser.close()

parser.process() # process the datum in the buffer and then clear the buffer
parser.forward() # forward the processed stream to the appropriate channel 


#Memebers:
parser.sep = '\t'
parser.endline = '\n'
parser.channels = {}
parser.errors = []
parser.start_time
parser.buffer
parser.processed
parser.datum_cnt
```



### `class Channel`

A `channel` is a datastream that is identified with a particlular `channel_id` and needs to be processed seperately. The channel is a temporary holding class for data and forwards the incoming data to an appropriate instance of a `DataForward class` (say a `LineBuffer`. The channel calls a `DataForward.feed(datum)` method that must be implemented by each of the `DataForward` classes.

```python
channel.channel_id
channel.feed(datum) #Accepts incoming datum
channel.forward() #→ calls DataForward.feed()
channel.datum #Holds data
channel.preprocesser = lambda datum : datum # A function (user-defined) that processes the 'held' data (optional)
channel.register_dataforward(DataForward) #Register a DataForward instance
channel.dataforward #Object reference where the data is forwarded 
```

  The `pyConsole` library provides a `LineBuffer` instance that will be used as a generic `DataForward` instance.

`port or file  --datum->  parser  --datum->  channel  --datum->  DataForward`



## Console

The console component is the main component of the library and handles the display of data, and handling of user IO.



### `class LineBuffer`

It is a list of lines (circular buffer / deque) . Apart from that, it contains some utility functions to manage the lines and conditionaing them for display. The class also implemets thread safety and concurrent access. The class has the following functions:

```python
lb.add() # Add line
lb.resize() # Resize buffer
lb.get_lines() # Returns a list of the lines in the buffer
lb.formatters #List of formatting functions that conditions the output texts
```






# Plans for Development

1. Create classes (simplest to hardest)
2. Integration tests (binary - two classes at a time)
3. Tests with a remote device
4. Beautification and feature addition.



→ How to create:

1. Create a file for a class
2. Add detailed doc string from the discussions.
3. Create basic structure (function signature only) and details documnetations for each function
4. Implemetation 