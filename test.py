filename = str(sys.argv[1])

#read the i_frame
i_frame_detected= cv2.imread(filename)

#get the current time which the time of the i_frame
i_frame_time= time.strftime("%H:%M:00")

#get all the jingles inside 2m folder as an example

jingles = Path().cwd().glob("**/*.png")

#compare the i_frame with each jingle

for jingle in jingles:
    #check the similarity between the two images
    result= compare_images(i_frame,jingle)
    
    # if they're not similar do nothing
    if result<0.5:
        pass
    
    else:  #they are similar
        
        logger.info('There is a similarity between this i_frame %s and this i_frame %s at %s',jingle,i_frame,i_frame_time)
        dif_time = i_frame_time - get_date_of_jingle(jingle)
        
        if dif_time==0:
            pass
        else:(base)
