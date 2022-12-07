from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_scope_operator = lazy_import('msgraph.generated.models.device_scope_operator')
device_scope_parameter = lazy_import('msgraph.generated.models.device_scope_parameter')
device_scope_status = lazy_import('msgraph.generated.models.device_scope_status')
entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsDeviceScope(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsDeviceScope and sets the default values.
        """
        super().__init__()
        # Indicates the creation date and time for the custom device scope.
        self._created_date_time: Optional[datetime] = None
        # The name of the user experience analytics device Scope configuration.
        self._device_scope_name: Optional[str] = None
        # Indicates whether a device scope is enabled or disabled. When TRUE, the device scope is enabled. When FALSE, the device scope is disabled. Default value is FALSE.
        self._enabled: Optional[bool] = None
        # Indicates whether the device scope configuration is built-in or custom. When TRUE, the device scope configuration is built-in. When FALSE, the device scope configuration is custom. Default value is FALSE.
        self._is_built_in: Optional[bool] = None
        # Indicates the last updated date and time for the custom device scope.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Device scope configuration query operator. Possible values are: equals, notEquals, contains, notContains, greaterThan, lessThan. Default value: equals.
        self._operator: Optional[device_scope_operator.DeviceScopeOperator] = None
        # The unique identifier of the person (admin) who created the device scope configuration.
        self._owner_id: Optional[str] = None
        # Device scope configuration parameter. It will be expend in future to add more parameter. Eg: device scope parameter can be OS version, Disk Type, Device manufacturer, device model or Scope tag. Default value: scopeTag.
        self._parameter: Optional[device_scope_parameter.DeviceScopeParameter] = None
        # Indicates the device scope status after the device scope has been enabled. Possible values are: none, computing, insufficientData or completed. Default value is none.
        self._status: Optional[device_scope_status.DeviceScopeStatus] = None
        # The device scope configuration query clause value.
        self._value: Optional[str] = None
        # The unique identifier for a user device scope tag Id used for the creation of device scope configuration.
        self._value_object_id: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Indicates the creation date and time for the custom device scope.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Indicates the creation date and time for the custom device scope.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsDeviceScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceScope
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsDeviceScope()
    
    @property
    def device_scope_name(self,) -> Optional[str]:
        """
        Gets the deviceScopeName property value. The name of the user experience analytics device Scope configuration.
        Returns: Optional[str]
        """
        return self._device_scope_name
    
    @device_scope_name.setter
    def device_scope_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceScopeName property value. The name of the user experience analytics device Scope configuration.
        Args:
            value: Value to set for the deviceScopeName property.
        """
        self._device_scope_name = value
    
    @property
    def enabled(self,) -> Optional[bool]:
        """
        Gets the enabled property value. Indicates whether a device scope is enabled or disabled. When TRUE, the device scope is enabled. When FALSE, the device scope is disabled. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabled property value. Indicates whether a device scope is enabled or disabled. When TRUE, the device scope is enabled. When FALSE, the device scope is disabled. Default value is FALSE.
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "device_scope_name": lambda n : setattr(self, 'device_scope_name', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "is_built_in": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(device_scope_operator.DeviceScopeOperator)),
            "owner_id": lambda n : setattr(self, 'owner_id', n.get_str_value()),
            "parameter": lambda n : setattr(self, 'parameter', n.get_enum_value(device_scope_parameter.DeviceScopeParameter)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(device_scope_status.DeviceScopeStatus)),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
            "value_object_id": lambda n : setattr(self, 'value_object_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_built_in(self,) -> Optional[bool]:
        """
        Gets the isBuiltIn property value. Indicates whether the device scope configuration is built-in or custom. When TRUE, the device scope configuration is built-in. When FALSE, the device scope configuration is custom. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._is_built_in
    
    @is_built_in.setter
    def is_built_in(self,value: Optional[bool] = None) -> None:
        """
        Sets the isBuiltIn property value. Indicates whether the device scope configuration is built-in or custom. When TRUE, the device scope configuration is built-in. When FALSE, the device scope configuration is custom. Default value is FALSE.
        Args:
            value: Value to set for the isBuiltIn property.
        """
        self._is_built_in = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Indicates the last updated date and time for the custom device scope.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Indicates the last updated date and time for the custom device scope.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def operator(self,) -> Optional[device_scope_operator.DeviceScopeOperator]:
        """
        Gets the operator property value. Device scope configuration query operator. Possible values are: equals, notEquals, contains, notContains, greaterThan, lessThan. Default value: equals.
        Returns: Optional[device_scope_operator.DeviceScopeOperator]
        """
        return self._operator
    
    @operator.setter
    def operator(self,value: Optional[device_scope_operator.DeviceScopeOperator] = None) -> None:
        """
        Sets the operator property value. Device scope configuration query operator. Possible values are: equals, notEquals, contains, notContains, greaterThan, lessThan. Default value: equals.
        Args:
            value: Value to set for the operator property.
        """
        self._operator = value
    
    @property
    def owner_id(self,) -> Optional[str]:
        """
        Gets the ownerId property value. The unique identifier of the person (admin) who created the device scope configuration.
        Returns: Optional[str]
        """
        return self._owner_id
    
    @owner_id.setter
    def owner_id(self,value: Optional[str] = None) -> None:
        """
        Sets the ownerId property value. The unique identifier of the person (admin) who created the device scope configuration.
        Args:
            value: Value to set for the ownerId property.
        """
        self._owner_id = value
    
    @property
    def parameter(self,) -> Optional[device_scope_parameter.DeviceScopeParameter]:
        """
        Gets the parameter property value. Device scope configuration parameter. It will be expend in future to add more parameter. Eg: device scope parameter can be OS version, Disk Type, Device manufacturer, device model or Scope tag. Default value: scopeTag.
        Returns: Optional[device_scope_parameter.DeviceScopeParameter]
        """
        return self._parameter
    
    @parameter.setter
    def parameter(self,value: Optional[device_scope_parameter.DeviceScopeParameter] = None) -> None:
        """
        Sets the parameter property value. Device scope configuration parameter. It will be expend in future to add more parameter. Eg: device scope parameter can be OS version, Disk Type, Device manufacturer, device model or Scope tag. Default value: scopeTag.
        Args:
            value: Value to set for the parameter property.
        """
        self._parameter = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deviceScopeName", self.device_scope_name)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_bool_value("isBuiltIn", self.is_built_in)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("operator", self.operator)
        writer.write_str_value("ownerId", self.owner_id)
        writer.write_enum_value("parameter", self.parameter)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("value", self.value)
        writer.write_str_value("valueObjectId", self.value_object_id)
    
    @property
    def status(self,) -> Optional[device_scope_status.DeviceScopeStatus]:
        """
        Gets the status property value. Indicates the device scope status after the device scope has been enabled. Possible values are: none, computing, insufficientData or completed. Default value is none.
        Returns: Optional[device_scope_status.DeviceScopeStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[device_scope_status.DeviceScopeStatus] = None) -> None:
        """
        Sets the status property value. Indicates the device scope status after the device scope has been enabled. Possible values are: none, computing, insufficientData or completed. Default value is none.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def value(self,) -> Optional[str]:
        """
        Gets the value property value. The device scope configuration query clause value.
        Returns: Optional[str]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[str] = None) -> None:
        """
        Sets the value property value. The device scope configuration query clause value.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    
    @property
    def value_object_id(self,) -> Optional[str]:
        """
        Gets the valueObjectId property value. The unique identifier for a user device scope tag Id used for the creation of device scope configuration.
        Returns: Optional[str]
        """
        return self._value_object_id
    
    @value_object_id.setter
    def value_object_id(self,value: Optional[str] = None) -> None:
        """
        Sets the valueObjectId property value. The unique identifier for a user device scope tag Id used for the creation of device scope configuration.
        Args:
            value: Value to set for the valueObjectId property.
        """
        self._value_object_id = value
    

