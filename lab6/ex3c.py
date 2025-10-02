def determine_progress1(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio == 0:
        progress = "Get going!"
    elif hits_spins_ratio > 0 and hits_spins_ratio < 0.25:
        progress = "On your way!"
    elif hits_spins_ratio >= 0.25 and hits_spins_ratio < 0.5:
        progress = "Almost there!"
    elif hits_spins_ratio >= 0.5 and hits < spins:
        progress = "You win!"
    else:
        progress = "Get going!"

    return progress

def test_determine_progress(progress_function1):
    assert progress_function1(10, 0) == "Get going!", " test case 1 fails"
    assert progress_function1(1, 5) == "On your way!", "test case 2 fails"
    assert progress_function1(1, 4) == "Almost there!", "test case 3 fails"
    assert progress_function1(5, 8) == "You win!", "test case 4 fails"
    assert progress_function1(4, 7) == "You win!", "test case 5 fails"
    assert progress_function1(1, 7) == "On your way!", "test case 6 fails"
    

test_determine_progress(determine_progress1)

