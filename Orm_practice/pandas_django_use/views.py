import pandas as pd
import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UploadForm
from .models import UploadedTranasaction

import logging

logger = logging.getLogger('pandas_django_use')

def upload_files(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        logger.debug(f"{files}")
        if form.is_valid():
            bank_name = form.cleaned_data['bank_name']
            transaction_type = form.cleaned_data['transaction_type']
            
            for file in files:
                try:
                    df = pd.read_csv(file)
                    logger.info(f"{df}")

                    # Clean column names: remove dots, replace spaces with underscores
                    df.columns = [re.sub(r'\s+', '_', col.strip().replace('.', '')) for col in df.columns]
                    logger.debug(f"{df.columns}")

                    # Update these indexes based on your actual file format
                    TXN_DATE = df.columns[1]
                    IRCTC_ORDER_NO = df.columns[2]
                    BANK_BOOKING_REF_NO = df.columns[3]
                    BOOKING_AMOUNT = df.columns[4]
                    CREDITED_ON = df.columns[5]

                    for _, row in df.iterrows():
                        UploadedTranasaction.objects.create(
                            bank_name=bank_name,
                            transaction_type=transaction_type,
                            TXN_DATE=row[TXN_DATE],
                            IRCTC_ORDER_NO=row[IRCTC_ORDER_NO],
                            BANK_BOOKING_REF_NO=row[BANK_BOOKING_REF_NO],
                            BOOKING_AMOUNT=row[BOOKING_AMOUNT],
                            CREDITED_ON=row[CREDITED_ON],
                        )
                    messages.success(request, f"{file.name} uploaded successfully!")
                except Exception as e:
                    messages.error(request, f"Failed to process {file.name}: {str(e)}")
            return redirect('upload_files')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})
