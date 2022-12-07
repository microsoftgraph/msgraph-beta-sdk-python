from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

comanagement_eligible_type = lazy_import('msgraph.generated.models.comanagement_eligible_type')
device_registration_state = lazy_import('msgraph.generated.models.device_registration_state')
device_type = lazy_import('msgraph.generated.models.device_type')
entity = lazy_import('msgraph.generated.models.entity')
management_agent_type = lazy_import('msgraph.generated.models.management_agent_type')
management_state = lazy_import('msgraph.generated.models.management_state')
owner_type = lazy_import('msgraph.generated.models.owner_type')

class ComanagementEligibleDevice(entity.Entity):
    """
    Device Co-Management eligibility state
    """
    @property
    def client_registration_status(self,) -> Optional[device_registration_state.DeviceRegistrationState]:
        """
        Gets the clientRegistrationStatus property value. Device registration status.
        Returns: Optional[device_registration_state.DeviceRegistrationState]
        """
        return self._client_registration_status
    
    @client_registration_status.setter
    def client_registration_status(self,value: Optional[device_registration_state.DeviceRegistrationState] = None) -> None:
        """
        Sets the clientRegistrationStatus property value. Device registration status.
        Args:
            value: Value to set for the clientRegistrationStatus property.
        """
        self._client_registration_status = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new comanagementEligibleDevice and sets the default values.
        """
        super().__init__()
        # Device registration status.
        self._client_registration_status: Optional[device_registration_state.DeviceRegistrationState] = None
        # DeviceName
        self._device_name: Optional[str] = None
        # Device type.
        self._device_type: Optional[device_type.DeviceType] = None
        # EntitySource
        self._entity_source: Optional[int] = None
        # Management agent type.
        self._management_agents: Optional[management_agent_type.ManagementAgentType] = None
        # Management state of device in Microsoft Intune.
        self._management_state: Optional[management_state.ManagementState] = None
        # Manufacturer
        self._manufacturer: Optional[str] = None
        # MDMStatus
        self._mdm_status: Optional[str] = None
        # Model
        self._model: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # OSDescription
        self._os_description: Optional[str] = None
        # OSVersion
        self._os_version: Optional[str] = None
        # Owner type of device.
        self._owner_type: Optional[owner_type.OwnerType] = None
        # ReferenceId
        self._reference_id: Optional[str] = None
        # SerialNumber
        self._serial_number: Optional[str] = None
        # The status property
        self._status: Optional[comanagement_eligible_type.ComanagementEligibleType] = None
        # UPN
        self._upn: Optional[str] = None
        # UserEmail
        self._user_email: Optional[str] = None
        # UserId
        self._user_id: Optional[str] = None
        # UserName
        self._user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ComanagementEligibleDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ComanagementEligibleDevice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ComanagementEligibleDevice()
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. DeviceName
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. DeviceName
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def device_type(self,) -> Optional[device_type.DeviceType]:
        """
        Gets the deviceType property value. Device type.
        Returns: Optional[device_type.DeviceType]
        """
        return self._device_type
    
    @device_type.setter
    def device_type(self,value: Optional[device_type.DeviceType] = None) -> None:
        """
        Sets the deviceType property value. Device type.
        Args:
            value: Value to set for the deviceType property.
        """
        self._device_type = value
    
    @property
    def entity_source(self,) -> Optional[int]:
        """
        Gets the entitySource property value. EntitySource
        Returns: Optional[int]
        """
        return self._entity_source
    
    @entity_source.setter
    def entity_source(self,value: Optional[int] = None) -> None:
        """
        Sets the entitySource property value. EntitySource
        Args:
            value: Value to set for the entitySource property.
        """
        self._entity_source = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "client_registration_status": lambda n : setattr(self, 'client_registration_status', n.get_enum_value(device_registration_state.DeviceRegistrationState)),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "device_type": lambda n : setattr(self, 'device_type', n.get_enum_value(device_type.DeviceType)),
            "entity_source": lambda n : setattr(self, 'entity_source', n.get_int_value()),
            "management_agents": lambda n : setattr(self, 'management_agents', n.get_enum_value(management_agent_type.ManagementAgentType)),
            "management_state": lambda n : setattr(self, 'management_state', n.get_enum_value(management_state.ManagementState)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "mdm_status": lambda n : setattr(self, 'mdm_status', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "os_description": lambda n : setattr(self, 'os_description', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "owner_type": lambda n : setattr(self, 'owner_type', n.get_enum_value(owner_type.OwnerType)),
            "reference_id": lambda n : setattr(self, 'reference_id', n.get_str_value()),
            "serial_number": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(comanagement_eligible_type.ComanagementEligibleType)),
            "upn": lambda n : setattr(self, 'upn', n.get_str_value()),
            "user_email": lambda n : setattr(self, 'user_email', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def management_agents(self,) -> Optional[management_agent_type.ManagementAgentType]:
        """
        Gets the managementAgents property value. Management agent type.
        Returns: Optional[management_agent_type.ManagementAgentType]
        """
        return self._management_agents
    
    @management_agents.setter
    def management_agents(self,value: Optional[management_agent_type.ManagementAgentType] = None) -> None:
        """
        Sets the managementAgents property value. Management agent type.
        Args:
            value: Value to set for the managementAgents property.
        """
        self._management_agents = value
    
    @property
    def management_state(self,) -> Optional[management_state.ManagementState]:
        """
        Gets the managementState property value. Management state of device in Microsoft Intune.
        Returns: Optional[management_state.ManagementState]
        """
        return self._management_state
    
    @management_state.setter
    def management_state(self,value: Optional[management_state.ManagementState] = None) -> None:
        """
        Sets the managementState property value. Management state of device in Microsoft Intune.
        Args:
            value: Value to set for the managementState property.
        """
        self._management_state = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. Manufacturer
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. Manufacturer
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def mdm_status(self,) -> Optional[str]:
        """
        Gets the mdmStatus property value. MDMStatus
        Returns: Optional[str]
        """
        return self._mdm_status
    
    @mdm_status.setter
    def mdm_status(self,value: Optional[str] = None) -> None:
        """
        Sets the mdmStatus property value. MDMStatus
        Args:
            value: Value to set for the mdmStatus property.
        """
        self._mdm_status = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. Model
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. Model
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    @property
    def os_description(self,) -> Optional[str]:
        """
        Gets the osDescription property value. OSDescription
        Returns: Optional[str]
        """
        return self._os_description
    
    @os_description.setter
    def os_description(self,value: Optional[str] = None) -> None:
        """
        Sets the osDescription property value. OSDescription
        Args:
            value: Value to set for the osDescription property.
        """
        self._os_description = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. OSVersion
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. OSVersion
        Args:
            value: Value to set for the osVersion property.
        """
        self._os_version = value
    
    @property
    def owner_type(self,) -> Optional[owner_type.OwnerType]:
        """
        Gets the ownerType property value. Owner type of device.
        Returns: Optional[owner_type.OwnerType]
        """
        return self._owner_type
    
    @owner_type.setter
    def owner_type(self,value: Optional[owner_type.OwnerType] = None) -> None:
        """
        Sets the ownerType property value. Owner type of device.
        Args:
            value: Value to set for the ownerType property.
        """
        self._owner_type = value
    
    @property
    def reference_id(self,) -> Optional[str]:
        """
        Gets the referenceId property value. ReferenceId
        Returns: Optional[str]
        """
        return self._reference_id
    
    @reference_id.setter
    def reference_id(self,value: Optional[str] = None) -> None:
        """
        Sets the referenceId property value. ReferenceId
        Args:
            value: Value to set for the referenceId property.
        """
        self._reference_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("clientRegistrationStatus", self.client_registration_status)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_enum_value("deviceType", self.device_type)
        writer.write_int_value("entitySource", self.entity_source)
        writer.write_enum_value("managementAgents", self.management_agents)
        writer.write_enum_value("managementState", self.management_state)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("mdmStatus", self.mdm_status)
        writer.write_str_value("model", self.model)
        writer.write_str_value("osDescription", self.os_description)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_enum_value("ownerType", self.owner_type)
        writer.write_str_value("referenceId", self.reference_id)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("upn", self.upn)
        writer.write_str_value("userEmail", self.user_email)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
    
    @property
    def serial_number(self,) -> Optional[str]:
        """
        Gets the serialNumber property value. SerialNumber
        Returns: Optional[str]
        """
        return self._serial_number
    
    @serial_number.setter
    def serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the serialNumber property value. SerialNumber
        Args:
            value: Value to set for the serialNumber property.
        """
        self._serial_number = value
    
    @property
    def status(self,) -> Optional[comanagement_eligible_type.ComanagementEligibleType]:
        """
        Gets the status property value. The status property
        Returns: Optional[comanagement_eligible_type.ComanagementEligibleType]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[comanagement_eligible_type.ComanagementEligibleType] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def upn(self,) -> Optional[str]:
        """
        Gets the upn property value. UPN
        Returns: Optional[str]
        """
        return self._upn
    
    @upn.setter
    def upn(self,value: Optional[str] = None) -> None:
        """
        Sets the upn property value. UPN
        Args:
            value: Value to set for the upn property.
        """
        self._upn = value
    
    @property
    def user_email(self,) -> Optional[str]:
        """
        Gets the userEmail property value. UserEmail
        Returns: Optional[str]
        """
        return self._user_email
    
    @user_email.setter
    def user_email(self,value: Optional[str] = None) -> None:
        """
        Sets the userEmail property value. UserEmail
        Args:
            value: Value to set for the userEmail property.
        """
        self._user_email = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. UserId
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. UserId
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. UserName
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. UserName
        Args:
            value: Value to set for the userName property.
        """
        self._user_name = value
    

