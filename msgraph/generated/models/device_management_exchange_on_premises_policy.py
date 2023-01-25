from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_exchange_access_level = lazy_import('msgraph.generated.models.device_management_exchange_access_level')
device_management_exchange_access_rule = lazy_import('msgraph.generated.models.device_management_exchange_access_rule')
device_management_exchange_device_class = lazy_import('msgraph.generated.models.device_management_exchange_device_class')
entity = lazy_import('msgraph.generated.models.entity')
on_premises_conditional_access_settings = lazy_import('msgraph.generated.models.on_premises_conditional_access_settings')

class DeviceManagementExchangeOnPremisesPolicy(entity.Entity):
    """
    Singleton entity which represents the Exchange OnPremises policy configured for a tenant.
    """
    @property
    def access_rules(self,) -> Optional[List[device_management_exchange_access_rule.DeviceManagementExchangeAccessRule]]:
        """
        Gets the accessRules property value. The list of device access rules in Exchange. The access rules apply globally to the entire Exchange organization
        Returns: Optional[List[device_management_exchange_access_rule.DeviceManagementExchangeAccessRule]]
        """
        return self._access_rules
    
    @access_rules.setter
    def access_rules(self,value: Optional[List[device_management_exchange_access_rule.DeviceManagementExchangeAccessRule]] = None) -> None:
        """
        Sets the accessRules property value. The list of device access rules in Exchange. The access rules apply globally to the entire Exchange organization
        Args:
            value: Value to set for the accessRules property.
        """
        self._access_rules = value
    
    @property
    def conditional_access_settings(self,) -> Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings]:
        """
        Gets the conditionalAccessSettings property value. The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
        Returns: Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings]
        """
        return self._conditional_access_settings
    
    @conditional_access_settings.setter
    def conditional_access_settings(self,value: Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings] = None) -> None:
        """
        Sets the conditionalAccessSettings property value. The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
        Args:
            value: Value to set for the conditionalAccessSettings property.
        """
        self._conditional_access_settings = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementExchangeOnPremisesPolicy and sets the default values.
        """
        super().__init__()
        # The list of device access rules in Exchange. The access rules apply globally to the entire Exchange organization
        self._access_rules: Optional[List[device_management_exchange_access_rule.DeviceManagementExchangeAccessRule]] = None
        # The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
        self._conditional_access_settings: Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings] = None
        # Access Level in Exchange.
        self._default_access_level: Optional[device_management_exchange_access_level.DeviceManagementExchangeAccessLevel] = None
        # The list of device classes known to Exchange
        self._known_device_classes: Optional[List[device_management_exchange_device_class.DeviceManagementExchangeDeviceClass]] = None
        # Notification text that will be sent to users quarantined by this policy. This is UTF8 encoded byte array HTML.
        self._notification_content: Optional[bytes] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementExchangeOnPremisesPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementExchangeOnPremisesPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementExchangeOnPremisesPolicy()
    
    @property
    def default_access_level(self,) -> Optional[device_management_exchange_access_level.DeviceManagementExchangeAccessLevel]:
        """
        Gets the defaultAccessLevel property value. Access Level in Exchange.
        Returns: Optional[device_management_exchange_access_level.DeviceManagementExchangeAccessLevel]
        """
        return self._default_access_level
    
    @default_access_level.setter
    def default_access_level(self,value: Optional[device_management_exchange_access_level.DeviceManagementExchangeAccessLevel] = None) -> None:
        """
        Sets the defaultAccessLevel property value. Access Level in Exchange.
        Args:
            value: Value to set for the defaultAccessLevel property.
        """
        self._default_access_level = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_rules": lambda n : setattr(self, 'access_rules', n.get_collection_of_object_values(device_management_exchange_access_rule.DeviceManagementExchangeAccessRule)),
            "conditional_access_settings": lambda n : setattr(self, 'conditional_access_settings', n.get_object_value(on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings)),
            "default_access_level": lambda n : setattr(self, 'default_access_level', n.get_enum_value(device_management_exchange_access_level.DeviceManagementExchangeAccessLevel)),
            "known_device_classes": lambda n : setattr(self, 'known_device_classes', n.get_collection_of_object_values(device_management_exchange_device_class.DeviceManagementExchangeDeviceClass)),
            "notification_content": lambda n : setattr(self, 'notification_content', n.get_bytes_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def known_device_classes(self,) -> Optional[List[device_management_exchange_device_class.DeviceManagementExchangeDeviceClass]]:
        """
        Gets the knownDeviceClasses property value. The list of device classes known to Exchange
        Returns: Optional[List[device_management_exchange_device_class.DeviceManagementExchangeDeviceClass]]
        """
        return self._known_device_classes
    
    @known_device_classes.setter
    def known_device_classes(self,value: Optional[List[device_management_exchange_device_class.DeviceManagementExchangeDeviceClass]] = None) -> None:
        """
        Sets the knownDeviceClasses property value. The list of device classes known to Exchange
        Args:
            value: Value to set for the knownDeviceClasses property.
        """
        self._known_device_classes = value
    
    @property
    def notification_content(self,) -> Optional[bytes]:
        """
        Gets the notificationContent property value. Notification text that will be sent to users quarantined by this policy. This is UTF8 encoded byte array HTML.
        Returns: Optional[bytes]
        """
        return self._notification_content
    
    @notification_content.setter
    def notification_content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the notificationContent property value. Notification text that will be sent to users quarantined by this policy. This is UTF8 encoded byte array HTML.
        Args:
            value: Value to set for the notificationContent property.
        """
        self._notification_content = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("accessRules", self.access_rules)
        writer.write_object_value("conditionalAccessSettings", self.conditional_access_settings)
        writer.write_enum_value("defaultAccessLevel", self.default_access_level)
        writer.write_collection_of_object_values("knownDeviceClasses", self.known_device_classes)
        writer.write_object_value("notificationContent", self.notification_content)
    

