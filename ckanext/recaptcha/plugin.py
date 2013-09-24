import ckan.plugins as plugins

# Our custom template helper function.
def show_recaptcha():
    '''Call this function to display the recaptach html/js snippet.'''

    return true 

class RecaptchaPlugin(plugins.SingletonPlugin):
    '''plugin interface for the Recaptcha feature for user creation.

    '''
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # Update CKAN's config settings, see the IConfigurer plugin interface.
    def update_config(self, config):

        # Tell CKAN where to find the templace files 
        plugins.toolkit.add_template_directory(config, 'templates')

    # Tell CKAN what custom template helper functions this plugin provides,
    # see the ITemplateHelpers plugin interface.
    def get_helpers(self):
        return {'recaptcha': show_recaptcha}
