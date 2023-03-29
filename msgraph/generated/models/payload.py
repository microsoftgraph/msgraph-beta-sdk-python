from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import email_identity, entity, payload_brand, payload_complexity, payload_delivery_platform, payload_detail, payload_industry, payload_theme, simulation_attack_technique, simulation_attack_type, simulation_content_source, simulation_content_status

from . import entity

class Payload(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new payload and sets the default values.
        """
        super().__init__()
        # The branch of a payload. Possible values are: unknown, other, americanExpress, capitalOne, dhl, docuSign, dropbox, facebook, firstAmerican, microsoft, netflix, scotiabank, stewartTitle, tesco, wellsFargo, syrinxCloud, adobe, teams, zoom, unknownFutureValue.
        self._brand: Optional[payload_brand.PayloadBrand] = None
        # The complexity of a payload.Possible values are: unknown, low, medium, high, unknownFutureValue
        self._complexity: Optional[payload_complexity.PayloadComplexity] = None
        # Identity of the user who created the attack simulation and training campaign payload.
        self._created_by: Optional[email_identity.EmailIdentity] = None
        # Date and time when the attack simulation and training campaign payload.
        self._created_date_time: Optional[datetime] = None
        # Description of the attack simulation and training campaign payload.
        self._description: Optional[str] = None
        # Additional details about the payload.
        self._detail: Optional[payload_detail.PayloadDetail] = None
        # Display name of the attack simulation and training campaign payload. Supports $filter and $orderby.
        self._display_name: Optional[str] = None
        # Industry of a payload. Possible values are: unknown, other, banking, businessServices, consumerServices, education, energy, construction, consulting, financialServices, government, hospitality, insurance, legal, courierServices, IT, healthcare, manufacturing, retail, telecom, realEstate, unknownFutureValue.
        self._industry: Optional[payload_industry.PayloadIndustry] = None
        # Indicates whether the attack simulation and training campaign payload was created from an automation flow. Supports $filter and $orderby.
        self._is_automated: Optional[bool] = None
        # Indicates whether the payload is controversial.
        self._is_controversial: Optional[bool] = None
        # Indicates whether the payload is from any recent event.
        self._is_current_event: Optional[bool] = None
        # Payload language.
        self._language: Optional[str] = None
        # Identity of the user who most recently modified the attack simulation and training campaign payload.
        self._last_modified_by: Optional[email_identity.EmailIdentity] = None
        # Date and time when the attack simulation and training campaign payload was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Free text tags for a payload.
        self._payload_tags: Optional[List[str]] = None
        # The payload delivery platform for a simulation. Possible values are: unknown, sms, email, teams, unknownFutureValue.
        self._platform: Optional[payload_delivery_platform.PayloadDeliveryPlatform] = None
        # Predicted probability for a payload to phish a targeted user.
        self._predicted_compromise_rate: Optional[float] = None
        # Attack type of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, social, cloud, endpoint, unknownFutureValue.
        self._simulation_attack_type: Optional[simulation_attack_type.SimulationAttackType] = None
        # The source property
        self._source: Optional[simulation_content_source.SimulationContentSource] = None
        # Simulation content status. Supports $filter and $orderby. Possible values are: unknown, draft, ready, archive, delete, unknownFutureValue. Inherited from simulation.
        self._status: Optional[simulation_content_status.SimulationContentStatus] = None
        # The social engineering technique used in the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, credentialHarvesting, attachmentMalware, driveByUrl, linkInAttachment, linkToMalwareFile, unknownFutureValue. For more information on the types of social engineering attack techniques, see simulations.
        self._technique: Optional[simulation_attack_technique.SimulationAttackTechnique] = None
        # The theme of a payload. Possible values are: unknown, other, accountActivation, accountVerification, billing, cleanUpMail, controversial, documentReceived, expense, incomingMessages, invoice, itemReceived, loginAlert, mailReceived, password, payment, payroll, personalizedOffer, quarantine, remoteWork, reviewMessage, securityUpdate, serviceSuspended, signatureRequired, upgradeMailboxStorage, verifyMailbox, voicemail, advertisement, employeeEngagement, unknownFutureValue.
        self._theme: Optional[payload_theme.PayloadTheme] = None
    
    @property
    def brand(self,) -> Optional[payload_brand.PayloadBrand]:
        """
        Gets the brand property value. The branch of a payload. Possible values are: unknown, other, americanExpress, capitalOne, dhl, docuSign, dropbox, facebook, firstAmerican, microsoft, netflix, scotiabank, stewartTitle, tesco, wellsFargo, syrinxCloud, adobe, teams, zoom, unknownFutureValue.
        Returns: Optional[payload_brand.PayloadBrand]
        """
        return self._brand
    
    @brand.setter
    def brand(self,value: Optional[payload_brand.PayloadBrand] = None) -> None:
        """
        Sets the brand property value. The branch of a payload. Possible values are: unknown, other, americanExpress, capitalOne, dhl, docuSign, dropbox, facebook, firstAmerican, microsoft, netflix, scotiabank, stewartTitle, tesco, wellsFargo, syrinxCloud, adobe, teams, zoom, unknownFutureValue.
        Args:
            value: Value to set for the brand property.
        """
        self._brand = value
    
    @property
    def complexity(self,) -> Optional[payload_complexity.PayloadComplexity]:
        """
        Gets the complexity property value. The complexity of a payload.Possible values are: unknown, low, medium, high, unknownFutureValue
        Returns: Optional[payload_complexity.PayloadComplexity]
        """
        return self._complexity
    
    @complexity.setter
    def complexity(self,value: Optional[payload_complexity.PayloadComplexity] = None) -> None:
        """
        Sets the complexity property value. The complexity of a payload.Possible values are: unknown, low, medium, high, unknownFutureValue
        Args:
            value: Value to set for the complexity property.
        """
        self._complexity = value
    
    @property
    def created_by(self,) -> Optional[email_identity.EmailIdentity]:
        """
        Gets the createdBy property value. Identity of the user who created the attack simulation and training campaign payload.
        Returns: Optional[email_identity.EmailIdentity]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[email_identity.EmailIdentity] = None) -> None:
        """
        Sets the createdBy property value. Identity of the user who created the attack simulation and training campaign payload.
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date and time when the attack simulation and training campaign payload.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date and time when the attack simulation and training campaign payload.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Payload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Payload
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Payload()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the attack simulation and training campaign payload.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the attack simulation and training campaign payload.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def detail(self,) -> Optional[payload_detail.PayloadDetail]:
        """
        Gets the detail property value. Additional details about the payload.
        Returns: Optional[payload_detail.PayloadDetail]
        """
        return self._detail
    
    @detail.setter
    def detail(self,value: Optional[payload_detail.PayloadDetail] = None) -> None:
        """
        Sets the detail property value. Additional details about the payload.
        Args:
            value: Value to set for the detail property.
        """
        self._detail = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the attack simulation and training campaign payload. Supports $filter and $orderby.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the attack simulation and training campaign payload. Supports $filter and $orderby.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import email_identity, entity, payload_brand, payload_complexity, payload_delivery_platform, payload_detail, payload_industry, payload_theme, simulation_attack_technique, simulation_attack_type, simulation_content_source, simulation_content_status

        fields: Dict[str, Callable[[Any], None]] = {
            "brand": lambda n : setattr(self, 'brand', n.get_enum_value(payload_brand.PayloadBrand)),
            "complexity": lambda n : setattr(self, 'complexity', n.get_enum_value(payload_complexity.PayloadComplexity)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(email_identity.EmailIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "detail": lambda n : setattr(self, 'detail', n.get_object_value(payload_detail.PayloadDetail)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_enum_value(payload_industry.PayloadIndustry)),
            "isAutomated": lambda n : setattr(self, 'is_automated', n.get_bool_value()),
            "isControversial": lambda n : setattr(self, 'is_controversial', n.get_bool_value()),
            "isCurrentEvent": lambda n : setattr(self, 'is_current_event', n.get_bool_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(email_identity.EmailIdentity)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "payloadTags": lambda n : setattr(self, 'payload_tags', n.get_collection_of_primitive_values(str)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(payload_delivery_platform.PayloadDeliveryPlatform)),
            "predictedCompromiseRate": lambda n : setattr(self, 'predicted_compromise_rate', n.get_float_value()),
            "simulationAttackType": lambda n : setattr(self, 'simulation_attack_type', n.get_enum_value(simulation_attack_type.SimulationAttackType)),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(simulation_content_source.SimulationContentSource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(simulation_content_status.SimulationContentStatus)),
            "technique": lambda n : setattr(self, 'technique', n.get_enum_value(simulation_attack_technique.SimulationAttackTechnique)),
            "theme": lambda n : setattr(self, 'theme', n.get_enum_value(payload_theme.PayloadTheme)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def industry(self,) -> Optional[payload_industry.PayloadIndustry]:
        """
        Gets the industry property value. Industry of a payload. Possible values are: unknown, other, banking, businessServices, consumerServices, education, energy, construction, consulting, financialServices, government, hospitality, insurance, legal, courierServices, IT, healthcare, manufacturing, retail, telecom, realEstate, unknownFutureValue.
        Returns: Optional[payload_industry.PayloadIndustry]
        """
        return self._industry
    
    @industry.setter
    def industry(self,value: Optional[payload_industry.PayloadIndustry] = None) -> None:
        """
        Sets the industry property value. Industry of a payload. Possible values are: unknown, other, banking, businessServices, consumerServices, education, energy, construction, consulting, financialServices, government, hospitality, insurance, legal, courierServices, IT, healthcare, manufacturing, retail, telecom, realEstate, unknownFutureValue.
        Args:
            value: Value to set for the industry property.
        """
        self._industry = value
    
    @property
    def is_automated(self,) -> Optional[bool]:
        """
        Gets the isAutomated property value. Indicates whether the attack simulation and training campaign payload was created from an automation flow. Supports $filter and $orderby.
        Returns: Optional[bool]
        """
        return self._is_automated
    
    @is_automated.setter
    def is_automated(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAutomated property value. Indicates whether the attack simulation and training campaign payload was created from an automation flow. Supports $filter and $orderby.
        Args:
            value: Value to set for the is_automated property.
        """
        self._is_automated = value
    
    @property
    def is_controversial(self,) -> Optional[bool]:
        """
        Gets the isControversial property value. Indicates whether the payload is controversial.
        Returns: Optional[bool]
        """
        return self._is_controversial
    
    @is_controversial.setter
    def is_controversial(self,value: Optional[bool] = None) -> None:
        """
        Sets the isControversial property value. Indicates whether the payload is controversial.
        Args:
            value: Value to set for the is_controversial property.
        """
        self._is_controversial = value
    
    @property
    def is_current_event(self,) -> Optional[bool]:
        """
        Gets the isCurrentEvent property value. Indicates whether the payload is from any recent event.
        Returns: Optional[bool]
        """
        return self._is_current_event
    
    @is_current_event.setter
    def is_current_event(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCurrentEvent property value. Indicates whether the payload is from any recent event.
        Args:
            value: Value to set for the is_current_event property.
        """
        self._is_current_event = value
    
    @property
    def language(self,) -> Optional[str]:
        """
        Gets the language property value. Payload language.
        Returns: Optional[str]
        """
        return self._language
    
    @language.setter
    def language(self,value: Optional[str] = None) -> None:
        """
        Sets the language property value. Payload language.
        Args:
            value: Value to set for the language property.
        """
        self._language = value
    
    @property
    def last_modified_by(self,) -> Optional[email_identity.EmailIdentity]:
        """
        Gets the lastModifiedBy property value. Identity of the user who most recently modified the attack simulation and training campaign payload.
        Returns: Optional[email_identity.EmailIdentity]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[email_identity.EmailIdentity] = None) -> None:
        """
        Sets the lastModifiedBy property value. Identity of the user who most recently modified the attack simulation and training campaign payload.
        Args:
            value: Value to set for the last_modified_by property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Date and time when the attack simulation and training campaign payload was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Date and time when the attack simulation and training campaign payload was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def payload_tags(self,) -> Optional[List[str]]:
        """
        Gets the payloadTags property value. Free text tags for a payload.
        Returns: Optional[List[str]]
        """
        return self._payload_tags
    
    @payload_tags.setter
    def payload_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the payloadTags property value. Free text tags for a payload.
        Args:
            value: Value to set for the payload_tags property.
        """
        self._payload_tags = value
    
    @property
    def platform(self,) -> Optional[payload_delivery_platform.PayloadDeliveryPlatform]:
        """
        Gets the platform property value. The payload delivery platform for a simulation. Possible values are: unknown, sms, email, teams, unknownFutureValue.
        Returns: Optional[payload_delivery_platform.PayloadDeliveryPlatform]
        """
        return self._platform
    
    @platform.setter
    def platform(self,value: Optional[payload_delivery_platform.PayloadDeliveryPlatform] = None) -> None:
        """
        Sets the platform property value. The payload delivery platform for a simulation. Possible values are: unknown, sms, email, teams, unknownFutureValue.
        Args:
            value: Value to set for the platform property.
        """
        self._platform = value
    
    @property
    def predicted_compromise_rate(self,) -> Optional[float]:
        """
        Gets the predictedCompromiseRate property value. Predicted probability for a payload to phish a targeted user.
        Returns: Optional[float]
        """
        return self._predicted_compromise_rate
    
    @predicted_compromise_rate.setter
    def predicted_compromise_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the predictedCompromiseRate property value. Predicted probability for a payload to phish a targeted user.
        Args:
            value: Value to set for the predicted_compromise_rate property.
        """
        self._predicted_compromise_rate = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("brand", self.brand)
        writer.write_enum_value("complexity", self.complexity)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_object_value("detail", self.detail)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("industry", self.industry)
        writer.write_bool_value("isAutomated", self.is_automated)
        writer.write_bool_value("isControversial", self.is_controversial)
        writer.write_bool_value("isCurrentEvent", self.is_current_event)
        writer.write_str_value("language", self.language)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("payloadTags", self.payload_tags)
        writer.write_enum_value("platform", self.platform)
        writer.write_float_value("predictedCompromiseRate", self.predicted_compromise_rate)
        writer.write_enum_value("simulationAttackType", self.simulation_attack_type)
        writer.write_enum_value("source", self.source)
        writer.write_enum_value("status", self.status)
        writer.write_enum_value("technique", self.technique)
        writer.write_enum_value("theme", self.theme)
    
    @property
    def simulation_attack_type(self,) -> Optional[simulation_attack_type.SimulationAttackType]:
        """
        Gets the simulationAttackType property value. Attack type of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, social, cloud, endpoint, unknownFutureValue.
        Returns: Optional[simulation_attack_type.SimulationAttackType]
        """
        return self._simulation_attack_type
    
    @simulation_attack_type.setter
    def simulation_attack_type(self,value: Optional[simulation_attack_type.SimulationAttackType] = None) -> None:
        """
        Sets the simulationAttackType property value. Attack type of the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, social, cloud, endpoint, unknownFutureValue.
        Args:
            value: Value to set for the simulation_attack_type property.
        """
        self._simulation_attack_type = value
    
    @property
    def source(self,) -> Optional[simulation_content_source.SimulationContentSource]:
        """
        Gets the source property value. The source property
        Returns: Optional[simulation_content_source.SimulationContentSource]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[simulation_content_source.SimulationContentSource] = None) -> None:
        """
        Sets the source property value. The source property
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    
    @property
    def status(self,) -> Optional[simulation_content_status.SimulationContentStatus]:
        """
        Gets the status property value. Simulation content status. Supports $filter and $orderby. Possible values are: unknown, draft, ready, archive, delete, unknownFutureValue. Inherited from simulation.
        Returns: Optional[simulation_content_status.SimulationContentStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[simulation_content_status.SimulationContentStatus] = None) -> None:
        """
        Sets the status property value. Simulation content status. Supports $filter and $orderby. Possible values are: unknown, draft, ready, archive, delete, unknownFutureValue. Inherited from simulation.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def technique(self,) -> Optional[simulation_attack_technique.SimulationAttackTechnique]:
        """
        Gets the technique property value. The social engineering technique used in the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, credentialHarvesting, attachmentMalware, driveByUrl, linkInAttachment, linkToMalwareFile, unknownFutureValue. For more information on the types of social engineering attack techniques, see simulations.
        Returns: Optional[simulation_attack_technique.SimulationAttackTechnique]
        """
        return self._technique
    
    @technique.setter
    def technique(self,value: Optional[simulation_attack_technique.SimulationAttackTechnique] = None) -> None:
        """
        Sets the technique property value. The social engineering technique used in the attack simulation and training campaign. Supports $filter and $orderby. Possible values are: unknown, credentialHarvesting, attachmentMalware, driveByUrl, linkInAttachment, linkToMalwareFile, unknownFutureValue. For more information on the types of social engineering attack techniques, see simulations.
        Args:
            value: Value to set for the technique property.
        """
        self._technique = value
    
    @property
    def theme(self,) -> Optional[payload_theme.PayloadTheme]:
        """
        Gets the theme property value. The theme of a payload. Possible values are: unknown, other, accountActivation, accountVerification, billing, cleanUpMail, controversial, documentReceived, expense, incomingMessages, invoice, itemReceived, loginAlert, mailReceived, password, payment, payroll, personalizedOffer, quarantine, remoteWork, reviewMessage, securityUpdate, serviceSuspended, signatureRequired, upgradeMailboxStorage, verifyMailbox, voicemail, advertisement, employeeEngagement, unknownFutureValue.
        Returns: Optional[payload_theme.PayloadTheme]
        """
        return self._theme
    
    @theme.setter
    def theme(self,value: Optional[payload_theme.PayloadTheme] = None) -> None:
        """
        Sets the theme property value. The theme of a payload. Possible values are: unknown, other, accountActivation, accountVerification, billing, cleanUpMail, controversial, documentReceived, expense, incomingMessages, invoice, itemReceived, loginAlert, mailReceived, password, payment, payroll, personalizedOffer, quarantine, remoteWork, reviewMessage, securityUpdate, serviceSuspended, signatureRequired, upgradeMailboxStorage, verifyMailbox, voicemail, advertisement, employeeEngagement, unknownFutureValue.
        Args:
            value: Value to set for the theme property.
        """
        self._theme = value
    

