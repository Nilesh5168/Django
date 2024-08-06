# /# views.py

# import os
# import pandas as pd
# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# import logging

# logger = logging.getLogger(__name__)

# def upload_file(request):
#     if request.method == 'POST' and request.FILES['document']:
#         try:
#             uploaded_file = request.FILES['document']
#             fs = FileSystemStorage()
#             filename = fs.save(uploaded_file.name, uploaded_file)
#             file_path = os.path.join(settings.MEDIA_ROOT, filename)
            
#             # Read the CSV file
#             data = pd.read_csv(file_path)

#             # Perform basic data analysis
#             first_rows = data.head()
#             summary_statistics = data.describe()
#             missing_values = data.isnull().sum()

#             # Convert Series objects to DataFrames
#             missing_values = missing_values.to_frame('Missing Values')

#             context = {
#                 'first_rows': first_rows.to_html(),
#                 'summary_statistics': summary_statistics.to_html(),
#                 'missing_values': missing_values.to_html(),
#                 'filename': filename,
#             }
#             return render(request, 'result.html', context)

#         except Exception as e:
#             logger.error("Error processing file upload: %s", e, exc_info=True)
#             return render(request, 'upload.html', {'error': str(e)})
    
#     return render(request, 'upload.html')


# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# import logging

# logger = logging.getLogger(__name__)

# def upload_file(request):
#     if request.method == 'POST' and request.FILES['document']:
#         try:
#             uploaded_file = request.FILES['document']
#             fs = FileSystemStorage()
#             filename = fs.save(uploaded_file.name, uploaded_file)
#             file_path = os.path.join(settings.MEDIA_ROOT, filename)
            
#             # Read the CSV file
#             data = pd.read_csv(file_path)

#             # Perform basic data analysis
#             first_rows = data.head()
#             summary_statistics = data.describe()
#             missing_values = data.isnull().sum()

#             # Convert Series objects to DataFrames
#             missing_values = missing_values.to_frame('Missing Values')

#             # Generate plots
#             if not os.path.exists(settings.MEDIA_ROOT):
#                 os.makedirs(settings.MEDIA_ROOT)

#             plot_paths = []
#             for column in data.select_dtypes(include=['float64', 'int64']).columns:
#                 plt.figure()
#                 sns.histplot(data[column].dropna(), kde=True)
#                 plot_path = os.path.join(settings.MEDIA_ROOT, f'{column}_histogram.png')
#                 plt.savefig(plot_path)
#                 plt.close()
#                 plot_paths.append(f'{column}_histogram.png')

#             context = {
#                 'first_rows': first_rows.to_html(),
#                 'summary_statistics': summary_statistics.to_html(),
#                 'missing_values': missing_values.to_html(),
#                 'filename': filename,
#                 'plot_paths': plot_paths,
#             }
#             return render(request, 'result.html', context)

#         except Exception as e:
#             logger.error("Error processing file upload: %s", e, exc_info=True)
#             return render(request, 'upload.html', {'error': str(e)})
    
#     return render(request, 'upload.html')




# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# import logging

# logger = logging.getLogger(__name__)

# def upload_file(request):
#     if request.method == 'POST' and request.FILES['document']:
#         try:
#             uploaded_file = request.FILES['document']
#             fs = FileSystemStorage()
#             filename = fs.save(uploaded_file.name, uploaded_file)
#             file_path = os.path.join(settings.MEDIA_ROOT, filename)
            
#             # Read the CSV file
#             data = pd.read_csv(file_path)

#             # Perform basic data analysis
#             first_rows = data.head()
#             summary_statistics = data.describe()
#             missing_values = data.isnull().sum()

#             # Convert Series objects to DataFrames
#             missing_values = missing_values.to_frame('Missing Values')

#             # Generate plots
#             if not os.path.exists(settings.MEDIA_ROOT):
#                 os.makedirs(settings.MEDIA_ROOT)

#             plot_paths = []
#             for column in data.select_dtypes(include=['float64', 'int64']).columns:
#                 plt.figure()
#                 sns.histplot(data[column].dropna(), kde=True)
#                 plot_path = os.path.join(settings.MEDIA_ROOT, f'{column}_histogram.png')
#                 plt.savefig(plot_path)
#                 plt.close()
#                 plot_paths.append(f'{column}_histogram.png')

#             context = {
#                 'first_rows': first_rows.to_html(),
#                 'summary_statistics': summary_statistics.to_html(),
#                 'missing_values': missing_values.to_html(),
#                 'filename': filename,
#                 'plot_paths': plot_paths,
#             }
#             return render(request, 'result.html', context)

#         except Exception as e:
#             logger.error("Error processing file upload: %s", e, exc_info=True)
#             return render(request, 'upload.html', {'error': str(e)})
    
#     return render(request, 'upload.html')


# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# import logging
# import matplotlib

# # Use the 'Agg' backend for rendering plots to files
# matplotlib.use('Agg')

# logger = logging.getLogger(__name__)

# def upload_file(request):
#     if request.method == 'POST' and request.FILES['document']:
#         try:
#             uploaded_file = request.FILES['document']
#             fs = FileSystemStorage()
#             filename = fs.save(uploaded_file.name, uploaded_file)
#             file_path = os.path.join(settings.MEDIA_ROOT, filename)
            
#             # Read the CSV file
#             data = pd.read_csv(file_path)

#             # Perform basic data analysis
#             first_rows = data.head()
#             summary_statistics = data.describe()
#             missing_values = data.isnull().sum()

#             # Convert Series objects to DataFrames
#             missing_values = missing_values.to_frame('Missing Values')

#             # Generate plots
#             plot_paths = []
#             for column in data.select_dtypes(include=['float64', 'int64']).columns:
#                 plt.figure()
#                 sns.histplot(data[column].dropna(), kde=True)
#                 plot_filename = f'{column}_histogram.png'
#                 plot_path = os.path.join(settings.MEDIA_ROOT, plot_filename)
#                 plt.savefig(plot_path)
#                 plt.close()
#                 plot_paths.append(os.path.join(settings.MEDIA_URL, plot_filename))

#             context = {
#                 'first_rows': first_rows.to_html(),
#                 'summary_statistics': summary_statistics.to_html(),
#                 'missing_values': missing_values.to_html(),
#                 'filename': filename,
#                 'plot_paths': plot_paths,
#             }
#             return render(request, 'result.html', context)

#         except Exception as e:
#             logger.error("Error processing file upload: %s", e, exc_info=True)
#             return render(request, 'upload.html', {'error': str(e)})
    
#     return render(request, 'upload.html')



import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import logging
import matplotlib
import base64
from io import BytesIO

# Use the 'Agg' backend for rendering plots to files
matplotlib.use('Agg')

logger = logging.getLogger(__name__)

def upload_file(request):
    if request.method == 'POST' and request.FILES['document']:
        try:
            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = os.path.join(settings.MEDIA_ROOT, filename)
            
            # Read the CSV file
            data = pd.read_csv(file_path)

            # Perform basic data analysis
            first_rows = data.head()
            summary_statistics = data.describe()
            missing_values = data.isnull().sum()

            # Convert Series objects to DataFrames
            missing_values = missing_values.to_frame('Missing Values')

            # Generate plots and encode them to base64
            plot_data = []
            for column in data.select_dtypes(include=['float64', 'int64']).columns:
                plt.figure()
                sns.histplot(data[column].dropna(), kde=True)
                buf = BytesIO()
                plt.savefig(buf, format='png')
                plt.close()
                buf.seek(0)
                image_base64 = base64.b64encode(buf.read()).decode('utf-8')
                plot_data.append({'name': column, 'data': image_base64})

            context = {
                'first_rows': first_rows.to_html(),
                'summary_statistics': summary_statistics.to_html(),
                'missing_values': missing_values.to_html(),
                'filename': filename,
                'plot_data': plot_data,
            }
            return render(request, 'result.html', context)

        except Exception as e:
            logger.error("Error processing file upload: %s", e, exc_info=True)
            return render(request, 'upload.html', {'error': str(e)})
    
    return render(request, 'upload.html')
