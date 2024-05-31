document.getElementById('exportButton').addEventListener('click', () => {
    const element = document.getElementById('content');
    const options = {
        margin: 1,
        filename: 'leviathan_threat_model.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'in', format: 'A4', orientation: 'portrait' }
    };
    html2pdf().from(element).set(options).save();
});