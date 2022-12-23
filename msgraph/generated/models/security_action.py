from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')
operation_status = lazy_import('msgraph.generated.models.operation_status')
result_info = lazy_import('msgraph.generated.models.result_info')
security_action_state = lazy_import('msgraph.generated.models.security_action_state')
security_vendor_information = lazy_import('msgraph.generated.models.security_vendor_information')

class SecurityAction(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def action_reason(self,) -> Optional[str]:
        """
        Gets the actionReason property value. Reason for invoking this action.
        Returns: Optional[str]
        """
        return self._action_reason
    
    @action_reason.setter
    def action_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the actionReason property value. Reason for invoking this action.
        Args:
            value: Value to set for the actionReason property.
        """
        self._action_reason = value
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The Application ID of the calling application that submitted (POST) the action. The appId should be extracted from the auth token and not entered manually by the calling application.
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The Application ID of the calling application that submitted (POST) the action. The appId should be extracted from the auth token and not entered manually by the calling application.
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    @property
    def azure_tenant_id(self,) -> Optional[str]:
        """
        Gets the azureTenantId property value. Azure tenant ID of the entity to determine which tenant the entity belongs to (multi-tenancy support). The azureTenantId should be extracted from the auth token and not entered manually by the calling application.
        Returns: Optional[str]
        """
        return self._azure_tenant_id
    
    @azure_tenant_id.setter
    def azure_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureTenantId property value. Azure tenant ID of the entity to determine which tenant the entity belongs to (multi-tenancy support). The azureTenantId should be extracted from the auth token and not entered manually by the calling application.
        Args:
            value: Value to set for the azureTenantId property.
        """
        self._azure_tenant_id = value
    
    @property
    def client_context(self,) -> Optional[str]:
        """
        Gets the clientContext property value. The clientContext property
        Returns: Optional[str]
        """
        return self._client_context
    
    @client_context.setter
    def client_context(self,value: Optional[str] = None) -> None:
        """
        Sets the clientContext property value. The clientContext property
        Args:
            value: Value to set for the clientContext property.
        """
        self._client_context = value
    
    @property
    def completed_date_time(self,) -> Optional[datetime]:
        """
        Gets the completedDateTime property value. Timestamp when the action was completed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDateTime property value. Timestamp when the action was completed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the completedDateTime property.
        """
        self._completed_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new securityAction and sets the default values.
        """
        super().__init__()
        # Reason for invoking this action.
        self._action_reason: Optional[str] = None
        # The Application ID of the calling application that submitted (POST) the action. The appId should be extracted from the auth token and not entered manually by the calling application.
        self._app_id: Optional[str] = None
        # Azure tenant ID of the entity to determine which tenant the entity belongs to (multi-tenancy support). The azureTenantId should be extracted from the auth token and not entered manually by the calling application.
        self._azure_tenant_id: Optional[str] = None
        # The clientContext property
        self._client_context: Optional[str] = None
        # Timestamp when the action was completed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._completed_date_time: Optional[datetime] = None
        # Timestamp when the action is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._created_date_time: Optional[datetime] = None
        # Error info when the action fails.
        self._error_info: Optional[result_info.ResultInfo] = None
        # Timestamp when this action was last updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._last_action_date_time: Optional[datetime] = None
        # Action name.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Collection of parameters (key-value pairs) necessary to invoke the action, for example, URL or fileHash to block.). Required.
        self._parameters: Optional[List[key_value_pair.KeyValuePair]] = None
        # Collection of securityActionState to keep the history of an action.
        self._states: Optional[List[security_action_state.SecurityActionState]] = None
        # Status of the action. Possible values are: NotStarted, Running, Completed, Failed.
        self._status: Optional[operation_status.OperationStatus] = None
        # The user principal name of the signed-in user that submitted  (POST) the action. The user should be extracted from the auth token and not entered manually by the calling application.
        self._user: Optional[str] = None
        # Complex Type containing details about the Security product/service vendor, provider, and sub-provider (for example, vendor=Microsoft; provider=Windows Defender ATP; sub-provider=AppLocker).
        self._vendor_information: Optional[security_vendor_information.SecurityVendorInformation] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Timestamp when the action is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Timestamp when the action is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecurityAction()
    
    @property
    def error_info(self,) -> Optional[result_info.ResultInfo]:
        """
        Gets the errorInfo property value. Error info when the action fails.
        Returns: Optional[result_info.ResultInfo]
        """
        return self._error_info
    
    @error_info.setter
    def error_info(self,value: Optional[result_info.ResultInfo] = None) -> None:
        """
        Sets the errorInfo property value. Error info when the action fails.
        Args:
            value: Value to set for the errorInfo property.
        """
        self._error_info = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_reason": lambda n : setattr(self, 'action_reason', n.get_str_value()),
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "azure_tenant_id": lambda n : setattr(self, 'azure_tenant_id', n.get_str_value()),
            "client_context": lambda n : setattr(self, 'client_context', n.get_str_value()),
            "completed_date_time": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "error_info": lambda n : setattr(self, 'error_info', n.get_object_value(result_info.ResultInfo)),
            "last_action_date_time": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parameters": lambda n : setattr(self, 'parameters', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "states": lambda n : setattr(self, 'states', n.get_collection_of_object_values(security_action_state.SecurityActionState)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(operation_status.OperationStatus)),
            "user": lambda n : setattr(self, 'user', n.get_str_value()),
            "vendor_information": lambda n : setattr(self, 'vendor_information', n.get_object_value(security_vendor_information.SecurityVendorInformation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActionDateTime property value. Timestamp when this action was last updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._last_action_date_time
    
    @last_action_date_time.setter
    def last_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActionDateTime property value. Timestamp when this action was last updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the lastActionDateTime property.
        """
        self._last_action_date_time = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Action name.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Action name.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def parameters(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the parameters property value. Collection of parameters (key-value pairs) necessary to invoke the action, for example, URL or fileHash to block.). Required.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._parameters
    
    @parameters.setter
    def parameters(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the parameters property value. Collection of parameters (key-value pairs) necessary to invoke the action, for example, URL or fileHash to block.). Required.
        Args:
            value: Value to set for the parameters property.
        """
        self._parameters = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("actionReason", self.action_reason)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("azureTenantId", self.azure_tenant_id)
        writer.write_str_value("clientContext", self.client_context)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("errorInfo", self.error_info)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("parameters", self.parameters)
        writer.write_collection_of_object_values("states", self.states)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("user", self.user)
        writer.write_object_value("vendorInformation", self.vendor_information)
    
    @property
    def states(self,) -> Optional[List[security_action_state.SecurityActionState]]:
        """
        Gets the states property value. Collection of securityActionState to keep the history of an action.
        Returns: Optional[List[security_action_state.SecurityActionState]]
        """
        return self._states
    
    @states.setter
    def states(self,value: Optional[List[security_action_state.SecurityActionState]] = None) -> None:
        """
        Sets the states property value. Collection of securityActionState to keep the history of an action.
        Args:
            value: Value to set for the states property.
        """
        self._states = value
    
    @property
    def status(self,) -> Optional[operation_status.OperationStatus]:
        """
        Gets the status property value. Status of the action. Possible values are: NotStarted, Running, Completed, Failed.
        Returns: Optional[operation_status.OperationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[operation_status.OperationStatus] = None) -> None:
        """
        Sets the status property value. Status of the action. Possible values are: NotStarted, Running, Completed, Failed.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def user(self,) -> Optional[str]:
        """
        Gets the user property value. The user principal name of the signed-in user that submitted  (POST) the action. The user should be extracted from the auth token and not entered manually by the calling application.
        Returns: Optional[str]
        """
        return self._user
    
    @user.setter
    def user(self,value: Optional[str] = None) -> None:
        """
        Sets the user property value. The user principal name of the signed-in user that submitted  (POST) the action. The user should be extracted from the auth token and not entered manually by the calling application.
        Args:
            value: Value to set for the user property.
        """
        self._user = value
    
    @property
    def vendor_information(self,) -> Optional[security_vendor_information.SecurityVendorInformation]:
        """
        Gets the vendorInformation property value. Complex Type containing details about the Security product/service vendor, provider, and sub-provider (for example, vendor=Microsoft; provider=Windows Defender ATP; sub-provider=AppLocker).
        Returns: Optional[security_vendor_information.SecurityVendorInformation]
        """
        return self._vendor_information
    
    @vendor_information.setter
    def vendor_information(self,value: Optional[security_vendor_information.SecurityVendorInformation] = None) -> None:
        """
        Sets the vendorInformation property value. Complex Type containing details about the Security product/service vendor, provider, and sub-provider (for example, vendor=Microsoft; provider=Windows Defender ATP; sub-provider=AppLocker).
        Args:
            value: Value to set for the vendorInformation property.
        """
        self._vendor_information = value
    

