%s1=serial('/dev/cu.usbmodem14201','BaudRate',115200);

%fopen(s1)

i=1;

%clear data;

h = animatedline('MaximumNumPoints',150); %create animatedline "object"
h.Color = 'red';
h2 = animatedline('MaximumNumPoints',150);
h2.Color = 'blue';
h3 = animatedline('MaximumNumPoints',150);
h3.Color = 'green';
h4 = animatedline('MaximumNumPoints',150);
h4.Color = 'black';
h5 = animatedline('MaximumNumPoints',150);
h5.Color = 'magenta';
axis([1,150,0,5])
x=linspace(1,150,150);
chan1=zeros(1,150); %initializing each channel vector
chan2=zeros(1,150);
chan3=zeros(1,150); 
chan4=zeros(1,150); 
chan5=zeros(1,150); 

datacoll=zeros(5,2000); %intilize storage matrix 

kk=1;

while(1)
    for k=1:length(x)
    chan1(k) = 2*str2double(fscanf(s1)); %read in each channel (convert from string to double)
    chan2(k) = str2double(fscanf(s1));
    chan3(k) = str2double(fscanf(s1));
    chan4(k) = str2double(fscanf(s1));
    chan5(k) = str2double(fscanf(s1));

  %  if i<=150
        %plot(data);
        addpoints(h,x(k),chan1(k)) %plot one point at a time 
        addpoints(h2,x(k),chan2(k))
        addpoints(h3,x(k),chan3(k))
        addpoints(h4,x(k),chan4(k))
        addpoints(h5,x(k),chan5(k))
 %   else
 %       addpoints(h,i,data(i))
        %plot(data(end-150:end))
 %   end

    %ylim([-100 2000]);
 %   ylim([-10 700]);

% The following if statement is for data recording of first 2000 pts.
 if kk<2001
    datacoll(1,kk)=chan1(k); %collect first 2000 point per channel
    datacoll(2,kk)=chan2(k);
    datacoll(3,kk)=chan3(k);
    datacoll(4,kk)=chan4(k);
    datacoll(5,kk)=chan5(k);
    kk=kk+1;
 end

    pause(0.001);
  drawnow
    end

  %  i = i+1;
  %  if i>150
  %      i=1;
  %  end
clearpoints(h) %clear points from graph (to start from beginning)
clearpoints(h2)
clearpoints(h3)
clearpoints(h4)
clearpoints(h5)
end

%fclose(s1)