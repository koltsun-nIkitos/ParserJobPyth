from headhunter import extract_max_page, extract_hh_jobs

hh_max_page = extract_max_page()
hh_jobs = extract_hh_jobs(hh_max_page)

print(hh_jobs)