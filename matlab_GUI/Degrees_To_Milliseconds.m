function [ Milliseconds  ] = Degrees_To_Milliseconds( Degrees )
Degrees = abs(Degrees);
Milliseconds = Degrees * 5.5555;                              %rough estimation
end

