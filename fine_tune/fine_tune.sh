cd /home/asi/camera/thamnt/det_train/meter_reg/train/data_roboflow/processed/v1
tesseract image_0.jpg training --psm 6 --dpi 70 lstm.train
mv training.lstmf image_0.lstmf
tesseract image_1.jpg training --psm 6 --dpi 70 lstm.train
mv training.lstmf image_1.lstmf

cd /home/asi/camera/thamnt/det_train/meter_reg/train_final
combine_tessdata -u /home/asi/camera/thamnt/det_train/meter_reg/ocr_system/tessdata/lets2.traineddata lets2.lstm

cd /home/asi/camera/thamnt/det_train/meter_reg/train/data_roboflow/processed/v1
ls -1 *.lstmf > lets2.training_files.txt

lstmeval --model /home/asi/camera/thamnt/det_train/meter_reg/train_final/model/lets2/lets2.lstm \
--traineddata /home/asi/camera/thamnt/det_train/meter_reg/ocr_system/tessdata/lets2.traineddata \
--eval_listfile /home/asi/camera/thamnt/det_train/meter_reg/train/data_roboflow/processed/v2/lets2.training_files.txt

lstmtraining --debug_interval -1 \
--continue_from /home/asi/camera/thamnt/det_train/meter_reg/train_final/model/lets2/lets2.lstm \
--model_output /home/asi/camera/thamnt/det_train/meter_reg/train_final/out/finetune3 \
--traineddata /home/asi/camera/thamnt/det_train/meter_reg/ocr_system/tessdata/lets2.traineddata \
--train_listfile /home/asi/camera/thamnt/det_train/meter_reg/train/data_roboflow/processed/v2/lets2.training_files.txt \
--max_iterations 2000



lstmtraining --stop_training \
--continue_from /home/asi/camera/thamnt/det_train/meter_reg/train_final/out/finetune3_2.568000_248_2000.checkpoint \
--traineddata /home/asi/camera/thamnt/det_train/meter_reg/ocr_system/tessdata/lets2.traineddata \
--model_output /home/asi/camera/thamnt/det_train/meter_reg/train_final/model/lets2/lets_finetuned3.traineddata

cd /home/asi/camera/thamnt/det_train/meter_reg/train_final/model/lets2
combine_tessdata -u /home/asi/camera/thamnt/det_train/meter_reg/train_final/model/lets2/lets_finetuned.traineddata ./

lstmeval --model /home/asi/camera/thamnt/det_train/meter_reg/train_final/model/lets2/.lstm \
--traineddata /home/asi/camera/thamnt/det_train/meter_reg/train_final/model/lets2/lets_finetuned.traineddata \
--eval_listfile /home/asi/camera/thamnt/det_train/meter_reg/train/data_roboflow/processed/v1/lets2.training_files.txt