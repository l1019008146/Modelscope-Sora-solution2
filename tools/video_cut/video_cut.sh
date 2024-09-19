export INPUT_CSV="${ROOT_META}/meta_clips_info_fmin1_aes_aesmin5.csv"
export OUTPUT_FOLDER="${ROOT_TIMECUT}"

# Cut raw videos
python ./tools/video_caption/scenedetect_vcut.py \
    --input_csv=$INPUT_CSV  \
    --threshold 10 20 30 \
    --frame_skip 0 1 2 \
    --min_seconds 1 \
    --max_seconds 5 \
    --save_dir $OUTPUT_FOLDER