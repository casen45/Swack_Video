from swack.video import VideoOverview


def main():
    vo = VideoOverview(video="test_video.mp4",
                       output="test_video.output.png",
                       w=3,
                       h=8,
                       shrink=0.5,
                       start_second=30,
                       end_second=100,
                       show_rank=False,
                       show_time=True,
                       save_thumbs=False,
                       )
    vo.run()


if __name__ == "__main__":
    main()
