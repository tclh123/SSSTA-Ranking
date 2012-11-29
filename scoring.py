#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tclh123'

from parser import *

def currentScore(spends, max_pts=1000.0, total=5*60.0):
    """ Time unit is mins, e.g. currentScore(22.7, 500.0, 60.0) = 293.95 """
    return max_pts*(0.3 + 0.7*total**2/(10*spends**2+total**2))

def scoring(html, prob_num, player_num, max_pts=1000.0):
    scores = {}

    p = Parser(html, prob_num, player_num)
    rank = p.parse()
    for username in rank:
        scores[username] = {}
        problems = [x for x in rank[username] if type(x)==int]
        for prob_id in problems:
            spends = rank[username][prob_id]
            if spends != '' and spends.find(':')!=-1:
                idx = spends.find('(')
                penalty = 0
                if idx!=-1:
                    penalty = int(spends[idx+2:-1])
                    spends = spends[:idx]
                t = map(int, spends.split(':'))
                scores[username][prob_id] = currentScore(t[0]*60+t[1]+t[2]/60.0+penalty*20, max_pts)
    return scores


if __name__ == "__main__":
    htmltest = "<table><tbody><tr><th>Rank</th><th>Id</th><th>Solve</th><th>Penalty</th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th></tr><tr><td>1</td><td>mizuki_tw</td><td>7</td><td>23:49:57</td><td>2:24:52(-5)</td><td>2:09:32(-3)</td><td>2:30:49</td><td>3:20:24(-2)</td><td>2:57:19(-1)</td><td>3:17:45</td><td>3:29:16</td><td></td></tr><tr><td>2</td><td>biamgo</td><td>7</td><td>24:10:13</td><td>2:27:22(-1)</td><td>2:46:14</td><td>3:05:14(-3)</td><td>3:14:22</td><td>3:31:13(-1)</td><td>3:39:16</td><td>3:46:32</td><td></td></tr><tr><td>3</td><td>ktboyyy</td><td>7</td><td>25:23:41</td><td>2:57:30(-5)</td><td>2:27:09</td><td>2:38:57</td><td>4:35:03(-2)</td><td>3:16:02</td><td>3:29:38</td><td>3:39:22</td><td></td></tr><tr><td>4</td><td>brotherroot</td><td>7</td><td>27:00:37</td><td>1:34:50(-2)</td><td>2:17:51(-5)</td><td>2:28:18(-1)</td><td>2:38:20</td><td>3:17:40(-7)</td><td>3:07:47(-1)</td><td>3:55:51(-7)</td><td></td></tr><tr><td>5</td><td>cripout</td><td>7</td><td>34:08:04</td><td>2:38:23(-5)</td><td>3:02:46(-1)</td><td>3:25:04(-1)</td><td>4:40:00(-2)</td><td>5:11:09(-5)</td><td>5:22:05</td><td>4:48:37(-1)</td><td></td></tr><tr><td>6</td><td>neveralso</td><td>7</td><td>34:23:34</td><td>2:43:47(-12)</td><td>2:35:28</td><td>2:40:37</td><td>6:01:28(-8)</td><td>3:11:44</td><td>5:32:14(-2)</td><td>3:58:16(-1)</td><td></td></tr><tr><td>7</td><td>gswxw</td><td>7</td><td>43:00:43</td><td>5:54:53(-13)</td><td>2:40:14</td><td>4:15:51(-5)</td><td>5:46:58(-4)</td><td>5:23:49</td><td>5:02:10(-1)</td><td>6:16:48</td><td></td></tr><tr><td>8</td><td>h549570564</td><td>7</td><td>45:21:08</td><td>5:56:42(-4)</td><td>3:55:32(-5)</td><td>4:12:00</td><td>6:53:57(-7)</td><td>5:41:32(-5)</td><td>5:05:37</td><td>6:35:48</td><td></td></tr><tr><td>9</td><td>perfect28</td><td>5</td><td>26:03:15</td><td>4:55:46(-5)</td><td>5:19:31(-3)</td><td>5:23:16(-1)</td><td>　(-4)</td><td>　(-8)</td><td>3:44:30</td><td>3:40:12</td><td></td></tr><tr><td>10</td><td>tclh123</td><td>4</td><td>11:56:44</td><td>2:35:18(-1)</td><td></td><td></td><td></td><td>3:00:14</td><td>3:00:28</td><td>3:00:44</td><td></td></tr><tr><td>11</td><td>lkid</td><td>3</td><td>14:13:10</td><td>3:31:45(-2)</td><td>4:49:11(-1)</td><td>4:52:14</td><td>　(-2)</td><td></td><td></td><td></td><td></td></tr><tr><td>12</td><td>z451538473</td><td>1</td><td>3:15:39</td><td>2:55:39(-1)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>13</td><td>frustratingman</td><td>1</td><td>3:45:07</td><td>3:45:07</td><td>　(-3)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>14</td><td>zzs1324</td><td>0</td><td>0:00:00</td><td>　(-7)</td><td>　(-1)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>"

    print scoring(htmltest, 7, 14)