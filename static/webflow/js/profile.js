// Profile page JS: handle permissions collapse chevron toggle
document.addEventListener('DOMContentLoaded', function () {
    var collapseEl = document.getElementById('permissionsCollapse');
    var toggle = document.getElementById('permissionsToggle');
    if (collapseEl && toggle) {
        collapseEl.addEventListener('show.bs.collapse', function () {
            var ico = toggle.querySelector('i'); if (ico) { ico.classList.remove('bi-chevron-down'); ico.classList.add('bi-chevron-up'); }
        });
        collapseEl.addEventListener('hide.bs.collapse', function () {
            var ico = toggle.querySelector('i'); if (ico) { ico.classList.remove('bi-chevron-up'); ico.classList.add('bi-chevron-down'); }
        });
    }
    
    // Inline email editing
    var editBtn = document.getElementById('emailEditBtn');
    var emailContainer = document.getElementById('emailContainer');
    var emailValue = document.getElementById('emailValue');
    var endpoint = emailContainer && emailContainer.dataset && emailContainer.dataset.endpoint ? emailContainer.dataset.endpoint : null;

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    if (editBtn && emailContainer && emailValue && endpoint) {
        editBtn.addEventListener('click', function (e) {
            e.preventDefault();
            var current = emailValue.textContent.trim();
            var input = document.createElement('input');
            input.type = 'email';
            input.className = 'form-control form-control-sm d-inline-block';
            input.style.maxWidth = '320px';
            input.value = current;
            input.id = 'emailEditInput';

            var saveBtn = document.createElement('button');
            saveBtn.className = 'btn btn-sm btn-primary ms-2';
            saveBtn.textContent = 'Save';
            saveBtn.id = 'emailSaveBtn';

            var cancelBtn = document.createElement('button');
            cancelBtn.className = 'btn btn-sm btn-outline-secondary ms-1';
            cancelBtn.textContent = 'Cancel';
            cancelBtn.id = 'emailCancelBtn';

            // Replace value span with input + buttons
            emailValue.style.display = 'none';
            editBtn.style.display = 'none';
            emailContainer.appendChild(input);
            emailContainer.appendChild(saveBtn);
            emailContainer.appendChild(cancelBtn);

            cancelBtn.addEventListener('click', function (ev) {
                ev.preventDefault();
                input.remove(); saveBtn.remove(); cancelBtn.remove();
                emailValue.style.display = ''; editBtn.style.display = '';
            });

            saveBtn.addEventListener('click', function (ev) {
                ev.preventDefault();
                var newEmail = input.value.trim();
                if (!newEmail) return;
                fetch(endpoint, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: 'email=' + encodeURIComponent(newEmail)
                }).then(function (res) {
                    if (!res.ok) throw res;
                    return res.json();
                }).then(function (data) {
                    emailValue.textContent = data.email;
                    input.remove(); saveBtn.remove(); cancelBtn.remove();
                    emailValue.style.display = ''; editBtn.style.display = '';
                    // small success feedback: append to top-level alerts container when available
                    var flash = document.createElement('div');
                    flash.className = 'alert alert-success alert-dismissible fade show';
                    flash.role = 'alert';
                    flash.innerHTML = 'Email updated successfully.<button type="button" class="btn-close" data-bs-dismiss="alert"></button>';
                    var target = document.getElementById('profileAlertsInner') || document.getElementById('profileAlerts') || emailContainer;
                    target.appendChild(flash);
                    // auto-dismiss after ~1.8s using Bootstrap Alert API if available
                    setTimeout(function () {
                        try {
                            if (window.bootstrap && bootstrap.Alert) {
                                bootstrap.Alert.getOrCreateInstance(flash).close();
                                return;
                            }
                        } catch (e) {
                            // ignore and fallback to remove
                        }
                        // fallback: remove element
                        if (flash && flash.parentNode) flash.parentNode.removeChild(flash);
                    }, 1800);
                }).catch(function (err) {
                    err.json().then(function (data) {
                        var msg = 'Unable to update email.';
                        if (data && data.errors && data.errors.email) msg = data.errors.email.join(' ');
                        var flash = document.createElement('div');
                        flash.className = 'alert alert-danger alert-dismissible fade show';
                        flash.role = 'alert';
                        flash.innerHTML = msg + '<button type="button" class="btn-close" data-bs-dismiss="alert"></button>';
                        var target = document.getElementById('profileAlertsInner') || document.getElementById('profileAlerts') || emailContainer;
                        target.appendChild(flash);
                        // auto-dismiss after ~1.8s using Bootstrap Alert API if available
                        setTimeout(function () {
                            try {
                                if (window.bootstrap && bootstrap.Alert) {
                                    bootstrap.Alert.getOrCreateInstance(flash).close();
                                    return;
                                }
                            } catch (e) {}
                            if (flash && flash.parentNode) flash.parentNode.removeChild(flash);
                        }, 1800);
                    }).catch(function () {
                        console.error('Email update failed');
                    });
                });
            });
        });
    }
});
