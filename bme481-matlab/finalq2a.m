%{
Q3: Curve Evolution
    a) Study the snake code, in UNR webcampus, and correlate it with the 
    derivations shown in the class. Experiment with the initial conditions shown in Panel 1, and 
    report results. The matlab code for initialization is provided. You need to make the synthetic 
    image. In each case, clearly show initial and final state of the curve evolution.
    (b) Now use the 
    code for Chan-Vese active contours without the edges by having many circles on the images and 
    show the evolution.
    (c) Apply Chan-Vese model to x-ray.jpg, show intermediate results and final 
    evolution. References are:
        https://www.mathworks.com/help/images/ref/activecontour.html#btuep4x-1-method 
        https://www.mathworks.com/matlabcentral/fileexchange/23445-chan-vese-active-contours-
        without-edges.
    The “method” is ‘Chan-vese,” which is default. The evolution should include at 
    least 8 seeds for initialization.  Show initial and final state of the level sets. 
%}

%% a.

% create synthetic image
% size of image
x = 400;
y = 200;

% circle parameters
centerX1 = 114;
centerX2 = 250; 
centerY = 100;
r = 76;

% fills areas outside circles
circles = zeros(y,x,'uint8');
for i = 1:x
    for j = 1:y
        if( (((i-centerX1)^2)+((j-centerY)^2)) <= r^2 )
            circles(j,i) = 255;
        end
        if( (((i-centerX2)^2)+((j-centerY)^2)) <= r^2 )
            circles(j,i) = 255;
        end
    end
end

% invert
Img = 255 - circles;

% show synthetic image

% apply gaussian blur to smooth circle
Img = imgaussfilt(Img,4);
Img = imsharpen(Img);
imshow(Img);

% snake integration
% figure 1
% x, y (Nx1 array) calculated from snakeinit.m
hold on
x = [];
y = [];
n =0;
% Loop, picking up the points
disp('Left mouse button picks points.')
disp('Right mouse button picks last point.')
but = 1;
while but == 1
      [s, t, but] = ginput(1);
      n = n + 1;
      x(n,1) = s;
      y(n,1) = t;
      plot(x, y, 'r-', 'Linewidth', 3);
end   
plot([x;x(1,1)],[y;y(1,1)],'r-', 'Linewidth', 3);

% fx, fy used gradient magnitude and direction of synthetic image 
[fx,fy] = imgradient(Img);

figure
imshow(Img);

[Xfig1, Yfig1] = snake(x, y, 0.1, 0.1, 0.5, 0.05, fx, fy, 0.4, 1, Img);
