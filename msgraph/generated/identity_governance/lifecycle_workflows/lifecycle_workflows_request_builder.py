from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

custom_task_extensions_request_builder = lazy_import('msgraph.generated.identity_governance.lifecycle_workflows.custom_task_extensions.custom_task_extensions_request_builder')
custom_task_extension_item_request_builder = lazy_import('msgraph.generated.identity_governance.lifecycle_workflows.custom_task_extensions.item.custom_task_extension_item_request_builder')
deleted_items_request_builder = lazy_import('msgraph.generated.identity_governance.lifecycle_workflows.deleted_items.deleted_items_request_builder')
settings_request_builder = lazy_import('msgraph.generated.identity_governance.lifecycle_workflows.settings.settings_request_builder')
task_definitions_request_builder = lazy_import('msgraph.generated.identity_governance.lifecycle_workflows.task_definitions.task_definitions_request_builder')
task_definition_item_request_builder = lazy_import('msgraph.generated.identity_governance.lifecycle_workflows.task_definitions.item.task_definition_item_request_builder')
workflows_request_builder = lazy_import('msgraph.generated.identity_governance.lifecycle_workflows.workflows.workflows_request_builder')
workflow_item_request_builder = lazy_import('msgraph.generated.identity_governance.lifecycle_workflows.workflows.item.workflow_item_request_builder')
workflow_templates_request_builder = lazy_import('msgraph.generated.identity_governance.lifecycle_workflows.workflow_templates.workflow_templates_request_builder')
workflow_template_item_request_builder = lazy_import('msgraph.generated.identity_governance.lifecycle_workflows.workflow_templates.item.workflow_template_item_request_builder')
lifecycle_workflows_container = lazy_import('msgraph.generated.models.identity_governance.lifecycle_workflows_container')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class LifecycleWorkflowsRequestBuilder():
    """
    Provides operations to manage the lifecycleWorkflows property of the microsoft.graph.identityGovernance entity.
    """
    @property
    def custom_task_extensions(self) -> custom_task_extensions_request_builder.CustomTaskExtensionsRequestBuilder:
        """
        Provides operations to manage the customTaskExtensions property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        """
        return custom_task_extensions_request_builder.CustomTaskExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deleted_items(self) -> deleted_items_request_builder.DeletedItemsRequestBuilder:
        """
        Provides operations to manage the deletedItems property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        """
        return deleted_items_request_builder.DeletedItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> settings_request_builder.SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        """
        return settings_request_builder.SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_definitions(self) -> task_definitions_request_builder.TaskDefinitionsRequestBuilder:
        """
        Provides operations to manage the taskDefinitions property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        """
        return task_definitions_request_builder.TaskDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def workflows(self) -> workflows_request_builder.WorkflowsRequestBuilder:
        """
        Provides operations to manage the workflows property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        """
        return workflows_request_builder.WorkflowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def workflow_templates(self) -> workflow_templates_request_builder.WorkflowTemplatesRequestBuilder:
        """
        Provides operations to manage the workflowTemplates property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        """
        return workflow_templates_request_builder.WorkflowTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new LifecycleWorkflowsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/lifecycleWorkflows{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[LifecycleWorkflowsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property lifecycleWorkflows for identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_get_request_information(self,request_configuration: Optional[LifecycleWorkflowsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get lifecycleWorkflows from identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[lifecycle_workflows_container.LifecycleWorkflowsContainer] = None, request_configuration: Optional[LifecycleWorkflowsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property lifecycleWorkflows in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def custom_task_extensions_by_id(self,id: str) -> custom_task_extension_item_request_builder.CustomTaskExtensionItemRequestBuilder:
        """
        Provides operations to manage the customTaskExtensions property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        Args:
            id: Unique identifier of the item
        Returns: custom_task_extension_item_request_builder.CustomTaskExtensionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["customTaskExtension%2Did"] = id
        return custom_task_extension_item_request_builder.CustomTaskExtensionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[LifecycleWorkflowsRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property lifecycleWorkflows for identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[LifecycleWorkflowsRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[lifecycle_workflows_container.LifecycleWorkflowsContainer]:
        """
        Get lifecycleWorkflows from identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[lifecycle_workflows_container.LifecycleWorkflowsContainer]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, lifecycle_workflows_container.LifecycleWorkflowsContainer, response_handler, error_mapping)
    
    async def patch(self,body: Optional[lifecycle_workflows_container.LifecycleWorkflowsContainer] = None, request_configuration: Optional[LifecycleWorkflowsRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[lifecycle_workflows_container.LifecycleWorkflowsContainer]:
        """
        Update the navigation property lifecycleWorkflows in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[lifecycle_workflows_container.LifecycleWorkflowsContainer]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, lifecycle_workflows_container.LifecycleWorkflowsContainer, response_handler, error_mapping)
    
    def task_definitions_by_id(self,id: str) -> task_definition_item_request_builder.TaskDefinitionItemRequestBuilder:
        """
        Provides operations to manage the taskDefinitions property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        Args:
            id: Unique identifier of the item
        Returns: task_definition_item_request_builder.TaskDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["taskDefinition%2Did"] = id
        return task_definition_item_request_builder.TaskDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def workflows_by_id(self,id: str) -> workflow_item_request_builder.WorkflowItemRequestBuilder:
        """
        Provides operations to manage the workflows property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        Args:
            id: Unique identifier of the item
        Returns: workflow_item_request_builder.WorkflowItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workflow%2Did"] = id
        return workflow_item_request_builder.WorkflowItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def workflow_templates_by_id(self,id: str) -> workflow_template_item_request_builder.WorkflowTemplateItemRequestBuilder:
        """
        Provides operations to manage the workflowTemplates property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        Args:
            id: Unique identifier of the item
        Returns: workflow_template_item_request_builder.WorkflowTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workflowTemplate%2Did"] = id
        return workflow_template_item_request_builder.WorkflowTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class LifecycleWorkflowsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class LifecycleWorkflowsRequestBuilderGetQueryParameters():
        """
        Get lifecycleWorkflows from identityGovernance
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class LifecycleWorkflowsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[LifecycleWorkflowsRequestBuilder.LifecycleWorkflowsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class LifecycleWorkflowsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

