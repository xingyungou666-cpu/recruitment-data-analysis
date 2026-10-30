from data_process.mysql_connect import get_connection


def save_job(job):
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        INSERT INTO jobs (
            job_id,
            keyword,
            job_area,
            job_name,
            job_salary,
            job_kind,
            job_degree,
            work_year,
            job_tags,
            co_name,
            co_size,
            co_kind,
            co_industry,
            publish_time,
            update_time
        )
        VALUES (
            %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s
        )
    """

    values = (
        job.get("jobid", ""),
        job.get("keyword",""),
        job.get("job_area", ""),
        job.get("job_name", ""),
        job.get("job_salary", ""),
        job.get("job_kind", ""),
        job.get("job_degree", ""),
        job.get("work_year", ""),
        job.get("job_tags", ""),
        job.get("co_name", ""),
        job.get("co_size", ""),
        job.get("co_kind", ""),
        job.get("co_industry", ""),
        job.get("publish_time",""),
        job.get("update_time","")
    )

    try:
        cursor.execute(sql, values)
        connection.commit()

        return "inserted"

    except Exception as e:

        connection.rollback()

        if "1062" in str(e):
            return "duplicate"

        return "error"

    finally:
        cursor.close()
        connection.close()