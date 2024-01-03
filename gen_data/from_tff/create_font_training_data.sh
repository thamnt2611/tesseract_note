python3 generate_training_txt.py
mv /home/asi/camera/thamnt/det_train/meter_reg/train_final/tessdata/7seg.traineddata /home/asi/camera/thamnt/det_train/meter_reg/train_final/tessdata/eng.traineddata
python3 -m tesstrain \
--fonts_dir /home/asi/camera/thamnt/det_train/meter_reg/train_final/fonts  \
--fontlist "Let's go Digital Bold Italic" \
--lang eng \
--linedata_only \
--langdata_dir /home/asi/camera/thamnt/det_train/meter_reg/train_final/langdata \
--tessdata_dir /home/asi/camera/thamnt/det_train/meter_reg/train_final/tessdata \
--save_box_tiff --maxpages 200 \
--output_dir /home/asi/camera/thamnt/det_train/meter_reg/train_final/data

combine_tessdata -e /home/asi/camera/thamnt/det_train/meter_reg/train_final/tessdata/eng.traineddata eng.lstm

lstmtraining --debug_interval -1 \
--continue_from /home/asi/camera/thamnt/det_train/meter_reg/train_final/eng.lstm \
--model_output /home/asi/camera/thamnt/det_train/meter_reg/train_final/model \
--traineddata /home/asi/camera/thamnt/det_train/meter_reg/train_final/tessdata/eng.traineddata \
--train_listfile /home/asi/camera/thamnt/det_train/meter_reg/train_final/data/eng.training_files.txt \
--max_iterations 400


lstmtraining --stop_training \
	--continue_from /home/asi/camera/thamnt/det_train/meter_reg/train_final/model/lets/model_checkpoint \
	--traineddata /home/asi/camera/thamnt/det_train/meter_reg/train_final/tessdata/eng.traineddata \
	--model_output /home/asi/camera/thamnt/det_train/meter_reg/train_final/model/lets/lets.traineddata