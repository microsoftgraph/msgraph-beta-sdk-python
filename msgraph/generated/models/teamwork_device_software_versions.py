from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TeamworkDeviceSoftwareVersions(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def admin_agent_software_version(self,) -> Optional[str]:
        """
        Gets the adminAgentSoftwareVersion property value. The software version for the admin agent running on the device.
        Returns: Optional[str]
        """
        return self._admin_agent_software_version
    
    @admin_agent_software_version.setter
    def admin_agent_software_version(self,value: Optional[str] = None) -> None:
        """
        Sets the adminAgentSoftwareVersion property value. The software version for the admin agent running on the device.
        Args:
            value: Value to set for the adminAgentSoftwareVersion property.
        """
        self._admin_agent_software_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkDeviceSoftwareVersions and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The software version for the admin agent running on the device.
        self._admin_agent_software_version: Optional[str] = None
        # The software version for the firmware running on the device.
        self._firmware_software_version: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The software version for the operating system on the device.
        self._operating_system_software_version: Optional[str] = None
        # The software version for the partner agent running on the device.
        self._partner_agent_software_version: Optional[str] = None
        # The software version for the Teams client running on the device.
        self._teams_client_software_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkDeviceSoftwareVersions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDeviceSoftwareVersions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkDeviceSoftwareVersions()
    
    @property
    def firmware_software_version(self,) -> Optional[str]:
        """
        Gets the firmwareSoftwareVersion property value. The software version for the firmware running on the device.
        Returns: Optional[str]
        """
        return self._firmware_software_version
    
    @firmware_software_version.setter
    def firmware_software_version(self,value: Optional[str] = None) -> None:
        """
        Sets the firmwareSoftwareVersion property value. The software version for the firmware running on the device.
        Args:
            value: Value to set for the firmwareSoftwareVersion property.
        """
        self._firmware_software_version = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "admin_agent_software_version": lambda n : setattr(self, 'admin_agent_software_version', n.get_str_value()),
            "firmware_software_version": lambda n : setattr(self, 'firmware_software_version', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operating_system_software_version": lambda n : setattr(self, 'operating_system_software_version', n.get_str_value()),
            "partner_agent_software_version": lambda n : setattr(self, 'partner_agent_software_version', n.get_str_value()),
            "teams_client_software_version": lambda n : setattr(self, 'teams_client_software_version', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def operating_system_software_version(self,) -> Optional[str]:
        """
        Gets the operatingSystemSoftwareVersion property value. The software version for the operating system on the device.
        Returns: Optional[str]
        """
        return self._operating_system_software_version
    
    @operating_system_software_version.setter
    def operating_system_software_version(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystemSoftwareVersion property value. The software version for the operating system on the device.
        Args:
            value: Value to set for the operatingSystemSoftwareVersion property.
        """
        self._operating_system_software_version = value
    
    @property
    def partner_agent_software_version(self,) -> Optional[str]:
        """
        Gets the partnerAgentSoftwareVersion property value. The software version for the partner agent running on the device.
        Returns: Optional[str]
        """
        return self._partner_agent_software_version
    
    @partner_agent_software_version.setter
    def partner_agent_software_version(self,value: Optional[str] = None) -> None:
        """
        Sets the partnerAgentSoftwareVersion property value. The software version for the partner agent running on the device.
        Args:
            value: Value to set for the partnerAgentSoftwareVersion property.
        """
        self._partner_agent_software_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("adminAgentSoftwareVersion", self.admin_agent_software_version)
        writer.write_str_value("firmwareSoftwareVersion", self.firmware_software_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatingSystemSoftwareVersion", self.operating_system_software_version)
        writer.write_str_value("partnerAgentSoftwareVersion", self.partner_agent_software_version)
        writer.write_str_value("teamsClientSoftwareVersion", self.teams_client_software_version)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def teams_client_software_version(self,) -> Optional[str]:
        """
        Gets the teamsClientSoftwareVersion property value. The software version for the Teams client running on the device.
        Returns: Optional[str]
        """
        return self._teams_client_software_version
    
    @teams_client_software_version.setter
    def teams_client_software_version(self,value: Optional[str] = None) -> None:
        """
        Sets the teamsClientSoftwareVersion property value. The software version for the Teams client running on the device.
        Args:
            value: Value to set for the teamsClientSoftwareVersion property.
        """
        self._teams_client_software_version = value
    

