
	exportRankHtml = ["<tr><th>Rank</th><th>Id</th><th>Solve</th><th>Penalty</th>"];
	for (var i = 0; i < pnum; i++) {
		exportRankHtml.push("<th>" + String.fromCharCode(65 + i) + "</th>")
	}
	exportRankHtml.push("</tr>");
	for (var i = 0; i < result.length; ++i) {
		var curInfo = result[i];
		var splitIdx = curInfo[0].lastIndexOf("_");
		var uid = curInfo[0].substr(0, splitIdx);
		var curCid = curInfo[0].substr(splitIdx + 1);
		if (showAllTeams == 0 && i >= 50 && (cid != curCid || !username[uid])) {
			continue;
		}
		exportRankHtml.push("<tr><td>" + (i + 1) + "</td><td>");
		if (username[uid]) {
			exportRankHtml.push((showNick > 0 ? nickname[uid] || username[uid] : username[uid]) + "</td>");
		} else {
			exportRankHtml.push(uid + "</td>");
		}
		var penaltyInHMS = dateFormat(curInfo[2], 0, 1);
		exportRankHtml.push("<td>" + curInfo[1] + "</td><td>" + penaltyInHMS + "</td>");

		var thisSb = sb[curInfo[0]];
		for (var j = 0; j <= pnum; ++j) {
			var probInfo = thisSb[j];
			if (!probInfo) {
				exportRankHtml.push("<td/>");
			} else {
				exportRankHtml.push("<td>" + dateFormat(probInfo[0], 0, 1) + (probInfo[1] ? "(-" + probInfo[1] + ")" : "") + "</td>");
			}
		}
		exportRankHtml.push("</tr>");
	}
	exportRankHtml = "<table>" + exportRankHtml.join("") + "</table>";