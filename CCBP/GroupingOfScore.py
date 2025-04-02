def get_color_score_pairs_dict(ball_score_list):
    color_scores_pairs_dict = {}
    for item in ball_score_list:
        pair = item.split(":")
        color, score = pair[0], int(pair[1])
        if color in color_scores_pairs_dict:
            color_scores_pairs_dict[color] = color_scores_pairs_dict[color] + score
        else:
            color_scores_pairs_dict[color] = score
    return color_scores_pairs_dict


# r:1,b:2,g:3,r:4

ball_score_list = input().split(",")
color_scores_pairs_dict = get_color_score_pairs_dict(ball_score_list)
print(color_scores_pairs_dict)



