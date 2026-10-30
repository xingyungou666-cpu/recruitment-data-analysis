def data_clean(job,keyword):
    jobid = job.get("jobid", "").strip()
    job_area = job.get("jobarea", "").strip()           #工作地点
    job_name = job.get("jobname", "").strip()           #工作名字
    job_salary = job.get("providesalary", "").strip()   #工资水平
    job_kind = job.get("jobterm", "").strip()           #工作性质
    job_degree = job.get("degree", "").strip()          #工作学历
    work_year = job.get("workyear", "").strip()         #工作年限
    job_tags = job.get("jobtag", "").strip()            #工作标签，其中还包含了福利，后面自行考虑是否保留

    co_name = job.get("coname", "").strip()
    co_size = job.get("cosize", "").strip()
    co_kind = job.get("cotype", "").strip()
    co_industry = job.get("coIndustryText", "").strip()

    publish_time = job.get("issuedate","").strip()
    update_time = job.get("lastupdate","").strip()

    job_function = job.get("funcType1Str", "").strip()  # 工作种类


    cleaned_job = {
            "jobid": jobid,
            "keyword":keyword,
            "job_area": job_area,
            "job_name": job_name,
            "job_salary": job_salary,
            "job_kind": job_kind,
            "job_degree": job_degree,
            "work_year": work_year,
            "job_tags": job_tags,

            "co_name": co_name,
            "co_size": co_size,
            "co_kind": co_kind,
            "co_Industry": co_industry,

            "publish_time":publish_time,
            "update_time":update_time,

            "job_function":job_function
        }

    return cleaned_job