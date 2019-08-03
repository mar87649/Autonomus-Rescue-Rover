function varargout = Main_GUI_Page(varargin)
% MAIN_GUI_PAGE MATLAB code for Main_GUI_Page.fig
%      MAIN_GUI_PAGE, by itself, creates a new MAIN_GUI_PAGE or raises the existing
%      singleton*.
%
%      H = MAIN_GUI_PAGE returns the handle to a new MAIN_GUI_PAGE or the handle to
%      the existing singleton*.
%
%      MAIN_GUI_PAGE('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in MAIN_GUI_PAGE.M with the given input arguments.
%
%      MAIN_GUI_PAGE('Property','Value',...) creates a new MAIN_GUI_PAGE or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Main_GUI_Page_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Main_GUI_Page_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Main_GUI_Page

% Last Modified by GUIDE v2.5 31-Oct-2018 18:59:59

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Main_GUI_Page_OpeningFcn, ...
                   'gui_OutputFcn',  @Main_GUI_Page_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before Main_GUI_Page is made visible.
function Main_GUI_Page_OpeningFcn(hObject, eventdata, handles, varargin)

handles.output = hObject;
SerialPort = serial('COM14','BaudRate',9600);   %defining serial port COM5 at 9600 baud
setappdata(0,'SerialPort',SerialPort);         %setting this serial port to app data.
pause on % to enable pause function
SerialPort.ReadAsyncMode = 'continuous';
SerialPort.BytesAvailableFcnCount = 1;
SerialPort.BytesAvailableFcnMode = 'byte';
SerialPort.BytesAvailableFcn = @Receive_Callback;



Directions_Array = [];
setappdata(0,'Directions_Array',Directions_Array)
Directions_Display_Array = {};
setappdata(0,'Directions_Display_Array',Directions_Display_Array)
set(handles.List_Of_Directions,'string',{});

guidata(hObject, handles);

function Receive_Callback()
SerialPort = getappdata(0,'SerialPort');
data = fread(SerialPort,'char');
disp(data);

% --- Outputs from this function are returned to the command line.
function varargout = Main_GUI_Page_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in Connect_To_Rover.
function Connect_To_Rover_Callback(hObject, eventdata, handles)
display('Connecting...')
fopen(getappdata(0,'SerialPort'));             %open the serial port
display('Connected.')


% --- Executes on button press in Disconnect_From_Rover.
function Disconnect_From_Rover_Callback(hObject, eventdata, handles)
display ('Disconnecting...')
fclose(getappdata(0,'SerialPort'));            %close serial port   
if ~isempty(instrfind)
    fclose(instrfind);
    delete(instrfind);
end
display ('Disconnected.')



function X_Coordinate_Callback(hObject, eventdata, handles)
% hObject    handle to X_Coordinate (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of X_Coordinate as text
%        str2double(get(hObject,'String')) returns contents of X_Coordinate as a double


% --- Executes during object creation, after setting all properties.
function X_Coordinate_CreateFcn(hObject, eventdata, handles)
% hObject    handle to X_Coordinate (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function Y_Coordinate_Callback(hObject, eventdata, handles)
% hObject    handle to Y_Coordinate (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Y_Coordinate as text
%        str2double(get(hObject,'String')) returns contents of Y_Coordinate as a double


% --- Executes during object creation, after setting all properties.
function Y_Coordinate_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Y_Coordinate (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function Rover_Direction_Callback(hObject, eventdata, handles)
% hObject    handle to Rover_Direction (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Rover_Direction as text
%        str2double(get(hObject,'String')) returns contents of Rover_Direction as a double


% --- Executes during object creation, after setting all properties.
function Rover_Direction_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Rover_Direction (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in Exit_Scanning_Mode.
function Exit_Scanning_Mode_Callback(hObject, eventdata, handles)
fprintf(getappdata(0,'SerialPort'),'B');       %send 'B' character to serial port


% --- Executes on button press in Enter_Scanning_Mode.
function Enter_Scanning_Mode_Callback(hObject, eventdata, handles)
fprintf(getappdata(0,'SerialPort'),'A');       %send 'A' character to serial port
%fread(SerialPort);




% --- Executes on button press in Enter_Path_Follower.
function Enter_Path_Follower_Callback(hObject, eventdata, handles)
fprintf(getappdata(0,'SerialPort'),'a');       %send 'a' character to serial port



% --- Executes on button press in Exit_Path_Follower.
function Exit_Path_Follower_Callback(hObject, eventdata, handles)

fprintf(getappdata(0,'SerialPort'),'a');       %send 'a' character to serial port


% --- Executes on selection change in List_Of_Directions.
function List_Of_Directions_Callback(hObject, eventdata, handles)
% hObject    handle to List_Of_Directions (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns List_Of_Directions contents as cell array
%        contents{get(hObject,'Value')} returns selected item from List_Of_Directions


% --- Executes during object creation, after setting all properties.
function List_Of_Directions_CreateFcn(hObject, eventdata, handles)
% hObject    handle to List_Of_Directions (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in Add_Direction.
function Add_Direction_Callback(hObject, eventdata, handles)
set(handles.List_Of_Directions,'value',1);
Add_Direction_GUI
uiwait(Add_Direction_GUI)
Duration = getappdata(0,'Duration_Value');
Direction = getappdata(0,'Direction_Value');
%[rows,columns] = size(getappdata(0,'Direction_Array'));
Array = getappdata(0,'Directions_Array');
Display_Array = getappdata(0,'Directions_Display_Array');
setappdata(0,'Directions_Array',[Array;Direction,Duration])
disp(getappdata(0,'Directions_Array'));
if (Direction == 1)
    str1 = 'Go forward for: ';
    str2 = num2str(Duration);
    str3 = ' milliseconds';
    Final_String = strcat(str1,str2,str3);
elseif (Direction == 2)
    str1 = 'Go left for: ';
    str2 = num2str(Duration);
    str3 = ' milliseconds';
    Final_String = strcat(str1,str2,str3);
elseif (Direction == 3)
    str1 = 'Go right for: ';
    str2 = num2str(Duration);
    str3 = ' milliseconds';
    Final_String = strcat(str1,str2,str3);
end

if (isempty(Display_Array))
setappdata(0,'Directions_Display_Array',{Final_String})
else
setappdata(0,'Directions_Display_Array',[Display_Array; Final_String])  
end
disp(getappdata(0,'Directions_Display_Array'))
set(handles.List_Of_Directions,'string',getappdata(0,'Directions_Display_Array'))

    
    



% --- Executes on button press in Remove_Direction.
function Remove_Direction_Callback(hObject, eventdata, handles)
if (~isempty(getappdata(0,'Directions_Array')))
rowToDelete = get(handles.List_Of_Directions,'value');
set(handles.List_Of_Directions,'value',1);
Array = getappdata(0,'Directions_Array');
Display_Array = getappdata(0,'Directions_Display_Array');
Array(rowToDelete, :) = [];
Display_Array(rowToDelete, :) = [];
setappdata(0,'Directions_Array', Array);
setappdata(0,'Directions_Display_Array',Display_Array);
set(handles.List_Of_Directions,'string',Display_Array);
end
% hObject    handle to Remove_Direction (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in Finish_Directions.
function Finish_Directions_Callback(hObject, eventdata, handles)
Transmit_All_Directions(getappdata(0,'Directions_Array'));
fprintf(getappdata(0,'SerialPort'),'d');       %send 'd' character to serial port


% --- Executes on button press in Begin_Directions.
function Begin_Directions_Callback(hObject, eventdata, handles)
fprintf(getappdata(0,'SerialPort'),'c');       %send 'a' character to serial port
